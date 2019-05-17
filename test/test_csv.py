import pytest
import os
import csv
from imdbdump.imdb_fetcher import ImdbFetcher

def test_json():
    imdb = ImdbFetcher('tt0303461')
    imdb.save_csv()
    with open('test/expected_firefly:_der_aufbruch_der_serenity.csv', 'r') as expected_csv_file:
        reader = csv.reader(expected_csv_file)
        expected_csv = list(map(tuple, reader))
    with open('output/firefly:_der_aufbruch_der_serenity.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_csv = list(map(tuple, reader))
    assert expected_csv == my_csv
    os.remove('output/firefly:_der_aufbruch_der_serenity.csv')