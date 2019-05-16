from requests_html import HTMLSession
import logging
import json
import csv
import sys
import argparse
import os

parser = argparse.ArgumentParser(description='Fetch ratings for every single episode of all seasons for a TV show and save it optionally to CSV oder JSON.')
parser.add_argument('-c', '--csv', dest='csv', action='store_true', default=False, help='Dump fetched data to CSV file.')
parser.add_argument('-j', '--json', dest='json', action='store_true', default=False, help='Dump fetched data to JSON file.')
parser.add_argument('shows', nargs=argparse.REMAINDER)

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)


class ImdbFetcher:
  """
  Class to fetch ratings for every single episode of all seasons for a TV show.
  """
  def __init__(self, tv_show):
    url = f'https://www.imdb.com/title/{tv_show}/episodes'
    session = HTMLSession()
    r = session.get(url)
    no_seasons = len(r.html.find('#bySeason > option'))
    self.title = r.html.find('#main > div.article.listo.list > div.subpage_title_block > div > h3 > a', first=True).text
    logging.info(f'Start parsing ratings of "{self.title}"..')

    self.ratings = []
    for i in range(1, int(no_seasons) + 1):
      url = f'https://www.imdb.com/title/{tv_show}/episodes?season={i}'
      r = session.get(url)
      season_ratings = [rating.find('span.ipl-rating-star__rating', first=True).text for rating in r.html.find('div.ipl-rating-star')][0::23]
      if season_ratings != []:
        self.ratings.append(season_ratings)
        logging.info(f'Ratings Season {i}: {season_ratings}')
  
    self._max_episodes_per_season = max(list(map(lambda x: len(x), self.ratings)))
    self._filename = f'{self.title.lower().replace(" ", "_")}'

    logging.info(f'Finished parsing {len(self.ratings)} season(s).')

  def _create_output(func):
    def wrapper(self):
      if not os.path.exists('output'):
        os.makedirs('output')
      func(self)
    return wrapper

  @_create_output
  def save_json(self):
    js = {}
    js[f'{self.title}'] = {}
    for s, season_ratings in enumerate(self.ratings):
      js[f'{self.title}'][f'S{s+1:02}'] = {}
      for e, rating in enumerate(season_ratings):
            js[f'{self.title}'][f'S{s+1:02}'][f'E{e+1:02}'] = rating     
    with open(f'output/{self._filename}.json', 'w') as json_file:
      json.dump(js, json_file, indent=2)
    logging.info(f'Ratings dumped to output/{self._filename}.json')

  @_create_output
  def save_csv(self):
    with open(f'output/{self._filename}.csv', mode='w') as csv_file:
      w = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      w.writerow(['Season'] + [f'E{i:02}' for i in range(1, self._max_episodes_per_season + 1)])
      for s, season_ratings in enumerate(self.ratings):
        w.writerow([f'S{s+1:02}'] + season_ratings)
    logging.info(f'Ratings dumped to output/{self._filename}.csv')


if __name__ == "__main__":
  args = parser.parse_args()
  
  for show in args.shows:
    imdb_fetcher = ImdbFetcher(show)
    if args.csv:
      imdb_fetcher.save_csv()
    if args.json:
      imdb_fetcher.save_json()