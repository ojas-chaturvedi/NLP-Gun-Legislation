#!/opt/homebrew/bin/python3
"""
Name: sentiment_analysis/initialize.py
Purpose: To initialize all the JSON files in sentiment_analysis/data with required data before the sentiment scores
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from json import JSONDecodeError, dump, load

from tqdm import tqdm


def initialize_data(session: int) -> None:
    """To initialize the JSON files with legislation name, date introduced, and party of sponsors

    Args:
        session (int): Congressional session number
    """

    with open(f"data_collection/data/{session}.json", "r") as f:
        legislative_texts = load(f)

    for category in legislative_texts.keys():
        for legislation in legislative_texts[category]:
            data = {
                "name": legislation["name"],
                "date_introduced": legislation["date_introduced"],
                "party_of_sponsors": legislation["party_of_sponsors"],
            }

            # Load existing data from file
            try:
                with open(f"sentiment_analysis/data/{session}.json", "r") as file:
                    try:
                        existing_data = load(file)
                    except JSONDecodeError:
                        existing_data = {}
            except FileNotFoundError:
                existing_data = {}

            if category not in existing_data:
                existing_data[category] = []
            existing_data[category].append(data)

            # Write back to the file
            with open(f"sentiment_analysis/data/{session}.json", "w") as file:
                dump(existing_data, file, indent=4)


if __name__ == "__main__":
    session_start = 107
    session_end = 117

    with tqdm(total=(session_end - session_start)) as progress_bar:
        for session in range(session_start, session_end + 1):
            initialize_data(session)
            progress_bar.update(1)
