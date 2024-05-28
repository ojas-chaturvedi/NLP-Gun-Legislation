#!/opt/homebrew/bin/python3
"""
Name: src/sentiment_analysis.py
Purpose: To run the sentiment analysis models and generate results / graphs using multiprocessing
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from csv import field_size_limit, reader, writer
from multiprocessing import Pool, cpu_count
from sys import maxsize

from sentiment_analysis.revert import session_end, session_start
from sentiment_analysis.vader_model import vader_model

field_size_limit(maxsize)


def main(session: int) -> None:
    print("-" * 30)
    print(f"Processing session {session}")

    with open(f"src/data/{session}.csv", "r") as f:
        read = reader(f)
        data = list(read)

    data[0].append("VADER Sentiment Score")

    for i in range(1, len(data)):
        sentiment = vader_model([data[i][-2]])
        data[i].append(sentiment)

    with open(f"src/data/{session}.csv", "w") as f:
        write = writer(f)
        write.writerows(data)


if __name__ == "__main__":
    # Remember to run src/sentiment_analysis/revert.py first before saving sentiment analysis model scores to CSV files

    sessions = range(session_start, session_end + 1)
    with Pool(cpu_count()) as p:
        p.map(main, sessions)
