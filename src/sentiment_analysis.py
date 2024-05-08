#!/opt/homebrew/bin/python3
"""
Name: sentiment_analysis/main.py
Purpose: To run the sentiment analysis models and generate results / graphs
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from csv import field_size_limit, reader, writer
from sys import maxsize

from tqdm import tqdm

# from sentiment_analysis.revert import session_end, session_start
from sentiment_analysis.vader_model import vader_model

session_start = 111
session_end = 115

field_size_limit(maxsize)


def main(session: int) -> None:
    with open(f"src/data/{session}.csv", "r") as f:
        read = reader(f)
        data = list(read)

    data[0].append("VADER Sentiment Score")

    with tqdm(total=len(data)) as progress_bar:
        for i in range(1, len(data)):
            sentiment = vader_model([data[i][-2]])
            data[i].append(sentiment)
            progress_bar.update(1)

    with open(f"src/data/{session}.csv", "w") as f:
        write = writer(f)
        write.writerows(data)


if __name__ == "__main__":
    # Remember to run sentiment_analysis/initialize.py first before saving sentiment analysis model scores to CSV files

    for session in range(session_start, session_end + 1):
        print("-" * 30)
        print(f"Session {session}")
        main(session)
