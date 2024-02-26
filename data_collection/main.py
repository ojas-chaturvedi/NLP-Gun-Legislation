#!/opt/homebrew/bin/python3
"""
File name / purpose
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"

import csv
from web_scraper import web_scraper

def main():
    # Open and read csv file
    file = open("URL_links.csv")
    reader = csv.reader(file)

    # Skip the first 6 rows with useless download information
    for i in range(6):
        next(reader)



if __name__ == "__main__":
    main()
