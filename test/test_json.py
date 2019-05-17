import pytest
import json
import os
from imdbdump.imdb_fetcher import ImdbFetcher

def test_json():
    imdb = ImdbFetcher('tt0303461')
    imdb.save_json()
    with open('test/expected_firefly:_der_aufbruch_der_serenity.json', 'r') as expected_js_file:
        expected_js = json.load(expected_js_file)
    with open('output/firefly:_der_aufbruch_der_serenity.json', 'r') as js_file:
        my_js = json.load(js_file)
    assert expected_js == my_js
    os.remove('output/firefly:_der_aufbruch_der_serenity.json')


