import pytest
import os
import csv
from imdbdump.imdb_fetcher import ImdbFetcher


def test_csv():
    imdb = ImdbFetcher('tt0141842')
    imdb.save_csv()
    with open('test/expected_the_sopranos.csv', 'r') as expected_csv_file:
        reader = csv.reader(expected_csv_file)
        expected_csv = list(map(tuple, reader))
    with open('output/the_sopranos.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        my_csv = [e for e in list(map(tuple, reader)) if e != ()]
    for expected_row, row in zip(expected_csv, my_csv):
        assert len(expected_row) == len(row)

    # cleanup
    os.remove('output/the_sopranos.csv')
