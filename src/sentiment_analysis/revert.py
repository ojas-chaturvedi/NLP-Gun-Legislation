#!/opt/homebrew/bin/python3
"""
Name: src/sentiment_analysis/revert.py
Purpose: To revert all the JSON files in src/data with required data before the sentiment scores
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


def revert_data(session: int) -> None:
    """To revert the CSV files back to legislative details without sentiment scores

    Args:
        session (int): Congressional session number
    """

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

    data_old = DictReader(open(f"src/data/{session}.csv", "r"))

    data_new = [headers]

    for legislation in data_old:
        data = [
            legislation["Name"],
            legislation["URL"],
            legislation["Legislation Type"],
            legislation["Session"],
            legislation["Date of Introduction"],
            legislation["Party of Sponsors"],
            legislation["Title"],
            legislation["Text"],
            legislation["Classification"],
        ]

        data_new.append(data)

    write = writer(open(f"src/data/{session}.csv", "w"))
    write.writerows(data_new)


if __name__ == "__main__":
    with tqdm(total=(session_end - session_start)) as progress_bar:
        for session in range(session_start, session_end + 1):
            revert_data(session)
            progress_bar.update(1)
