#!/opt/homebrew/bin/python3
"""
Main file for data collection script
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"


from web_scraper import web_scraper
from csv import reader
from time import time
from itertools import islice
from json import load, dump, JSONDecodeError


def main():
    # Open and read csv file, while skipping the first 6 rows with useless bulk download information
    file = open("data_collection/URL_links.csv")
    rows = reader(islice(file, 6, None))

    # Print all modified legislation links
    # Run web_scraper script in all legislation links
    for row in rows:
        name = row[0]
        url = row[1]
        type = get_legislation_type(name)
        text = web_scraper(url)
        save_data(type, name, url, text)

    # Close file to be more memory-efficient
    file.close()


def save_data(type, name, url, text):
    # Construct data object
    data = {
        "name": name,
        "url": url,
        "text": text,
    }

    # Load existing data from file
    try:
        with open("data_collection/data.json", "r") as file:
            try:
                existing_data = load(file)
            except JSONDecodeError:
                existing_data = {}
    except FileNotFoundError:
        existing_data = {}

    # Append new data under the bill type
    if type not in existing_data:
        existing_data[type] = []
    existing_data[type].append(data)

    # Write back to file
    with open("data_collection/data.json", "w") as file:
        dump(existing_data, file, indent=4)


def get_legislation_type(name):
    # Types of legislation
    legislation_types = {
        "H.R.": "House Bill",
        "H.Res.": "House Resolution",
        "H.J.Res.": "House Joint Resolution",
        "H.Con.Res.": "House Concurrent Resolution",
        "S.": "Senate Bill",
        "S.Res.": "Senate Resolution",
        "S.J.Res.": "Senate Joint Resolution",
        "S.Con.Res.": "Senate Concurrent Resolution",
    }

    # Split name into legislation abbreviation and number
    abbreviation = (name.split())[0]

    # Look up the full name based on the abbreviation
    full_name = legislation_types.get(abbreviation)
    if full_name is not None:
        return full_name
    else:
        # Handle case where abbreviation is not found
        return "Unknown Type"


if __name__ == "__main__":
    # Run function and see how long it takes
    start_time = time()

    main()

    end_time = time()
    execution_time = end_time - start_time
    print(execution_time)
