from setuptools import find_packages, setup
with open('README.md') as f:
    long_description = f.read()

setup(
    description = 'sqlaclhemy mapping of db, used in muscraper ELT.',
    url = 'URL to get it at.',
    long_description = long_description,
    author = 'Maytham Alherz',
    author_email = 'gmaytham@gmail.com',
    version = '0.0.1',
    packages = ['mualchemy'],
    install_requires=['SQLAlchemy>=1.3.13 ','PyYAML>=5.3 ','psycopg2>=2.8.4 '],
    name = 'mualchemy',
    license = 'Apache 2.0',
)

