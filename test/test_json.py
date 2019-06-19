import pytest
import json
import os
from imdbdump.imdb_fetcher import ImdbFetcher


def test_json():
    imdb = ImdbFetcher('tt0141842')
    imdb.save_json()
    with open('test/expected_the_sopranos.json', 'r') as expected_js_file:
        expected_js = json.load(expected_js_file)
    with open('output/the_sopranos.json', 'r') as js_file:
        my_js = json.load(js_file)

    # assert same amount of seasons
    assert len(expected_js[imdb.title]) == len(my_js[imdb.title])

    # assert same amount of episodes per season
    for i in range(1, len(my_js[imdb.title]) + 1):
        assert len(expected_js[imdb.title][f'S{i:02}']) == len(my_js[imdb.title][f'S{i:02}'])

    # cleanup
    os.remove('output/the_sopranos.json')



