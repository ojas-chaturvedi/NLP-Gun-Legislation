#!/opt/homebrew/bin/python3
"""
Main file for data collection script
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"


from web_scraper import web_scraper
from csv import reader
from itertools import islice
from time import time
from json import load, dump, JSONDecodeError


def main():
    # Open and read CSV file, skipping the first 6 rows with bulk download information
    with open("data_collection/URL_links.csv") as file:
        rows = reader(islice(file, 6, None))

        # Process each row in the CSV file
        for row in rows:
            name = row[0]
            url = row[1]
            session = row[2]
            title = row[3]

            # Determine the type of legislation based on its name abbreviation
            legislation_type = get_legislation_type(name)

            # Clean session text to just include number of session and not years /
            session = clean_session_text(session)

            # Scrape the web content from the URL
            text = web_scraper(url)

            save_data(legislation_type, name, url, session, title, text)

    # Close file to be more memory-efficient
    file.close()


def save_data(type, name, url, session, title, text):
    # Construct data object
    data = {
        "name": name,
        "url": url,
        "session": session,
        "title": title,
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


def clean_session_text(session):
    # Split the session by word
    session_parts = session.split()

    # Extract the session number with suffix
    session_number_with_suffix = session_parts[0]

    # Remove the suffix by slicing the string
    session_number_without_suffix = session_number_with_suffix[:3]

    print(session_number_without_suffix)

    return session_number_without_suffix


if __name__ == "__main__":
    # Run function and see how long it takes
    start_time = time()

    main()

    end_time = time()
    execution_time = end_time - start_time
    print(execution_time)
