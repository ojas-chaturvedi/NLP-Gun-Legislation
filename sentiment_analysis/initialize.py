#!/opt/homebrew/bin/python3
"""
Name: sentiment_analysis/initialize.py
Purpose: To initialize all the JSON files in sentiment_analysis/data with required data before the sentiment scores
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"


from csv import DictReader, field_size_limit, writer
from sys import maxsize

from tqdm import tqdm

field_size_limit(maxsize)

session_start = 101
session_end = 117


def initialize_data(session: int) -> None:
    """To initialize the CSV files with legislation name, date introduced, and party of sponsors

    Args:
        session (int): Congressional session number
    """

    headers = [
        "Name",
        "Session",
        "Date of Introduction",
        "Party of Sponsors",
        "Classification",
    ]

    data_f = open(f"data_collection/data/{session}.csv", "r")
    legislative_data = DictReader(data_f)

    with open(f"sentiment_analysis/data/{session}.csv", "w") as sentiment_f:
        write = writer(sentiment_f)
        write.writerow(headers)

        for legislation in legislative_data:
            data = [
                legislation["Name"],
                legislation["Session"],
                legislation["Date of Introduction"],
                legislation["Party of Sponsors"],
                legislation["Classification"],
            ]

            write.writerow(data)

    data_f.close()


if __name__ == "__main__":
    with tqdm(total=(session_end - session_start)) as progress_bar:
        for session in range(session_start, session_end + 1):
            initialize_data(session)
            progress_bar.update(1)
