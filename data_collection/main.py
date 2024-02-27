#!/opt/homebrew/bin/python3
"""
Main file for data collection script
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"

from csv import reader
from web_scraper import web_scraper
from time import time
from itertools import islice


def main():
    # Open and read csv file, while skipping the first 6 rows with useless bulk download information
    file = open("data_collection/URL_links.csv")
    rows = reader(islice(file, 6, None))

    # Print all modified legislation links
    # Run web_scraper script in all legislation links
    for row in rows:
        print(row[1] + "/text?format=txt")
        web_scraper(row[1] + "/text?format=txt")

    # Close file to be more memory-efficient
    file.close()


from firebase_admin import *


def testing_database():
    cred = credentials.Certificate("data_collection/firebase_credentials.json")
    initialize_app(
        cred,
        {"databaseURL": "https://nlp-gun-legislation-default-rtdb.firebaseio.com/"},
    )


if __name__ == "__main__":
    # Run function and see how long it takes
    start_time = time()
    # main()
    testing_database
    end_time = time()
    execution_time = end_time - start_time
    print(execution_time)
