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
from itertools import islice



def main():
    # Open and read csv file, while skipping the first 6 rows with useless bulk download information
    file = open("data_collection/URL_links.csv")
    reader = csv.reader(islice(file, 6, None))

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
