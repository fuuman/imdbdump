# IMDbDump
[![Build Status](https://travis-ci.com/fuuman/imdbdump.svg?token=dNr9gvKCz2cmaPy1fg3m&branch=master)](https://travis-ci.com/fuuman/imdbdump)
[![Coverage Status](https://coveralls.io/repos/github/fuuman/imdbdump/badge.svg?branch=master)](https://coveralls.io/github/fuuman/imdbdump?branch=master)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Updates](https://pyup.io/repos/github/fuuman/imdbdump/shield.svg)](https://pyup.io/repos/github/fuuman/imdbdump/)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/fuuman)


IMDbDump is a small library that provides the functionality to parse imdb.com for all single episode ratings for TV shows. The main focus lays on fetching IMDb data and save it in machine-readable formats to do some data science and visualization stuff with it. It's easily possible to dump fetched information to a JSON or CSV file. You can use the command line interface or import it in your own code.

## Installation
```
pip install imdbdump
```

## Usage
The input is always the unique id of that TV show on imdb.com. </br>
_Example_: https://www.imdb.com/title/tt0944947/ for 'Game Of Thrones'. `tt0944947` would be the needed parameter.
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
