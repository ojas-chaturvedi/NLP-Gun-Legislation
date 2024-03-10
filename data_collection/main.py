#!/opt/homebrew/bin/python3
"""
Name: data_collection/main.py
Purpose: To collect the data for the sentiment analysis models
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"

from web_scraper import web_scraper
from csv import reader
from itertools import islice
from time import time
from json import load, dump, JSONDecodeError


def main(csv_file_path: str) -> None:
    # Open and read CSV file, skipping the first 6 rows with bulk download information
    with open(csv_file_path) as file:
        rows = reader(islice(file, 6, None))

        # Process each row in the CSV file
        for row in rows:
            name = row[0]
            url = row[1]
            session = row[2]
            title = row[3]
            party = row[4]
            date = row[5]

            # Determine the type of legislation based on its name abbreviation
            legislation_type = get_legislation_type(name)

            # Clean session text to just include number of session and not years
            session = clean_session_text(session)

            # Scrape the web content from the URL
            text = web_scraper(url)

            save_data(party, name, url, legislation_type, session, date, title, text)

    # Close file to be more memory-efficient
    file.close()


def save_data(
    party: str,
    name: str,
    url: str,
    type: str,
    session: str,
    date: str,
    title: str,
    text: str,
) -> None:
    # Construct data object
    data = {
        "name": name,
        "url": url,
        "bill_type": type,
        "session": session,
        "date_introduced": date,
        "title": title,
        "text": text,
    }

    # Load existing data from file
    try:
        with open(f"data_collection/{session}.json", "r") as file:
            try:
                existing_data = load(file)
            except JSONDecodeError:
                existing_data = {}
    except FileNotFoundError:
        existing_data = {}

    # Append new data under the bill party sponsor
    if party not in existing_data:
        existing_data[party] = []
    existing_data[party].append(data)

    # Write back to file
    with open(f"data_collection/{session}.json", "w") as file:
        dump(existing_data, file, indent=4)


def get_legislation_type(name: str) -> str:
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


def clean_session_text(session: str) -> str:
    # Split the session by word
    session_parts = session.split()

    # Extract the session number with suffix
    session_number_with_suffix = session_parts[0]

    # Remove the suffix by slicing the string
    session_number_without_suffix = session_number_with_suffix[:3]

    return session_number_without_suffix


def find_duplicate_titles(csv_file_path: str) -> map:
    # Dictionary to store titles and their corresponding legislation numbers
    title_legislation_map = {}

    # List to store duplicate titles
    duplicate_titles = []

    # Open and read CSV file, skipping the first 6 rows with bulk download information
    with open(csv_file_path) as file:
        rows = reader(islice(file, 6, None))

        # Process each row in the CSV file
        for row in rows:
            title = row[3]
            legislation_number = row[0]

            # Check if title already exists in the map
            if title in title_legislation_map:
                # If title is already in the map, add it to duplicate_titles list
                if title not in duplicate_titles:
                    duplicate_titles.append(title)
                # Append the current legislation number to the existing list of legislation numbers for this title
                title_legislation_map[title].append(legislation_number)
            else:
                # If title is not in the map, add it to the map with its legislation number
                title_legislation_map[title] = [legislation_number]

    # Close file
    file.close()

    # Return duplicate titles along with their legislation numbers
    return {title: title_legislation_map[title] for title in duplicate_titles}


if __name__ == "__main__":
    # Run function and see how long it takes
    start_time = time()

    duplicate_titles_map = find_duplicate_titles("data_collection/URL_links.csv")
    for title, legislation_numbers in duplicate_titles_map.items():
        print(
            f"Title '{title}' is duplicated with legislation numbers: {legislation_numbers}"
        )

    main("data_collection/URL_links.csv")

    end_time = time()
    execution_time = end_time - start_time
    print(execution_time)
