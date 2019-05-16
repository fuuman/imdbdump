from setuptools import setup

setup(name='imdbdump',
      version='0.1.1',
      description='Helps you to dump TV show IMDb ratings in machine-readable formats.',
      url='http://github.com/fuuman/imdbdump',
      author='Marco Schanz',
      author_email='mschanz1210@gmail.com',
      license='GNU GPLv3',
      packages=['imdbdump'],
      install_requires=['requests-html'],
      zip_safe=False)
