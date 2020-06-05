import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='search-this',
    version='0.4.2',
    packages=['search_this'],
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='Get search results from Google and DuckDuckGo',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Artem Kotik',
    author_email='miaow2@ya.ru',
    keywords=['otus'],
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'search_this = search_this.start:start',
        ]
    },
)