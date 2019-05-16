from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='imdbdump',
      version='0.1.2',
      description='Helps you to dump TV show IMDb ratings in machine-readable formats.',
      url='http://github.com/fuuman/imdbdump',
      author='Marco Schanz',
      author_email='mschanz1210@gmail.com',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='GNU GPLv3',
      packages=['imdbdump'],
      install_requires=['requests-html'],
      zip_safe=False)
