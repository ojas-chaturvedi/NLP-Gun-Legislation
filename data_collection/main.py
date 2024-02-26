#!/opt/homebrew/bin/python3
"""
File name / purpose
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"

import csv
from web_scraper import web_scraper
from time import time


def main():
    # Open and read csv file
    file = open("URL_links.csv")
    reader = csv.reader(file)

    # Skip the first 6 rows with useless download information
    for i in range(6):
        next(reader)

    # Append all legislation-info rows to list
    rows = []
    for row in reader:
        rows.append(row)

    # Close file to be more memory-efficient
    file.close()

    # Print out all of the legislation links
    for row in rows:
        print(row[1])
        print("\n")


if __name__ == "__main__":
    # Run function and see how long it takes
    start_time = time()
    main()
    end_time = time()
    execution_time = end_time - start_time
    print(execution_time)
