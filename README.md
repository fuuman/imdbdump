# IMDbDump
IMDbDump is a small library that provides the functionality to parse imdb.com for all single episode ratings for TV shows. It's easily possible to dump this information to a JSON or CSV file. You can use the command line interface or import it in your own code.

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
