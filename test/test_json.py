import pytest
import json
import os
from imdbdump.imdb_fetcher import ImdbFetcher

def test_json():
    imdb = ImdbFetcher('tt0141842')
    imdb.save_json()
    with open('test/expected_die_sopranos.json', 'r') as expected_js_file:
        expected_js = json.load(expected_js_file)
    with open('output/die_sopranos.json', 'r') as js_file:
        my_js = json.load(js_file)
    assert expected_js == my_js
    os.remove('output/die_sopranos.json')


