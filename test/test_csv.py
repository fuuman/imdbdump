import pytest
import os
import csv
from imdbdump.imdb_fetcher import ImdbFetcher

def test_json():
    imdb = ImdbFetcher('tt0141842')
    imdb.save_csv()
    with open('test/expected_the_sopranos.csv', 'r') as expected_csv_file:
        reader = csv.reader(expected_csv_file)
        expected_csv = list(map(tuple, reader))
    with open('output/the_sopranos.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_csv = list(map(tuple, reader))
    assert expected_csv == my_csv
    os.remove('output/the_sopranos.csv')