#!/opt/homebrew/bin/python3
"""
Name: src/data_collection.py
Purpose: To collect the data for the sentiment analysis models
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from csv import field_size_limit, reader, writer
from itertools import islice
from os import makedirs, path
from subprocess import run
from sys import maxsize

from data_collection.classification import classification
from data_collection.scraper import web_scraper

field_size_limit(maxsize)


def main(csv_file_path: str) -> None:
    # Open and read CSV file, skipping the first 6 rows with bulk download information
    with open(csv_file_path) as file:
        rows = reader(islice(file, 6, None))

        # Initialize a variable to keep track of the previous session string.
        previous_session = None

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

            # If there is a new session for legislation, send a notification to phone
            if session != previous_session:
                initialize_csv(session)
                send_notification(session)
                previous_session = session

            # Scrape the web content from the URL
            text = web_scraper(url)

            classification_type = classification(text)

            save_data(
                name,
                url,
                legislation_type,
                session,
                date,
                party,
                title,
                text,
                classification_type,
            )


def initialize_csv(session: str) -> None:
    headers = [
        "Name",
        "URL",
        "Legislation Type",
        "Session",
        "Date of Introduction",
        "Party of Sponsors",
        "Title",
        "Text",
        "Classification",
    ]

    # Ensure the directory exists
    directory = "src/data/"
    if not path.exists(directory):
        makedirs(directory)

    with open(f"src/data/{session}.csv", "w") as f:
        write = writer(f)

        write.writerow(headers)


def save_data(
    name: str,
    url: str,
    type: str,
    session: str,
    date: str,
    party: str,
    title: str,
    text: str,
    classification: str,
) -> None:
    # Construct data object
    data = [
        name,
        url,
        type,
        session,
        date,
        party,
        title,
        text,
        classification,
    ]

    with open(f"src/data/{session}.csv", "a") as f:
        write = writer(f)

        write.writerow(data)


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


# Note: this function utilizes the ntfy package, which can be downloaded here: https://ntfy.sh/
def send_notification(session: str) -> None:
    run(
        [
            "ntfy",
            "publish",
            "nlp-gun-control",
            "Running session number:",
            session,
        ]
    )


if __name__ == "__main__":
    # To find duplicate legislation (based off of title, legislation text may differ):
    # duplicate_titles_map = find_duplicate_titles("data_collection/URL_links.csv")
    # for title, legislation_numbers in duplicate_titles_map.items():
    #     print(
    #         f"Title '{title}' is duplicated with legislation numbers: {legislation_numbers}"
    #     )

    main("src/URL_links.csv")
