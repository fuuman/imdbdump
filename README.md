# IMDbDump
IMDbDump is a small library that provides the functionality to parse imdb.com for all single episode ratings for TV shows. The main focus lays on fetching IMDb data and save it in machine-readable formats to do some data science and visualization stuff with it. It's easily possible to dump fetched information to a JSON or CSV file. You can use the command line interface or import it in your own code.

## Installation
```
pip install imdbdump
```

## Usage
### CLI
```
python imdb_fetcher.py --json --csv tt0944947
```

### Importing
```python
from imdbdump.imdb_fetcher import ImdbFetcher

imdb = ImdbFetcher('tt0944947')
imdb.save_csv()
imdb.save_json()
```
