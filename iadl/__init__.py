# Package metada
__version__ = "1.0.0"
__author__ = "vichmartins"
__description__ = "A Python package to scrape and download files from the Internet Archive."

from iad.scraper import InternetArchiveScraper
from iad.downloader import FileDownloader
from iad.cli import main

# Define __all__ to specify what gets imported with `from iad import *`
__all__ = ["InternetArchiveScraper", "FileDownloader", "main"]