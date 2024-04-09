#!/opt/homebrew/bin/python3
"""
Name: sentiment_analysis/main.py
Purpose: To run the sentiment analysis models and generate results / graphs
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from json import load

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from data_collection.main import get_legislation_count
from vader_model import vader_model


def main() -> None:
    print("Hello World!")


def general_score_average_checker(legislation_type: str, session: int) -> None:
    sentiment_counts = {
        "positive": 0,
        "negative": 0,
        "neutral": 0,
    }

    with open(f"../data_collection/data/{session}.json", "r") as f:
        legislative_texts = load(f)

    legislation_count = len(legislative_texts[legislation_type])

    with tqdm(total=legislation_count) as progress_bar:
        for legislation in legislative_texts[legislation_type]:
            score = vader_model(legislation["text"])
            sentiment_counts[score] += 1
            progress_bar.update(1)

    print(f"Session {session} -- Section {legislation_type}")
    print(sentiment_counts)


def create_graph() -> None:
    start_session = 114
    end_session = 117

    data: dict = {}

    for session in range(start_session, end_session + 1):
        compound_all: float = 0
        count: int = 0

        with open(f"data_collection/data/{session}.json", "r") as f:
            legislative_texts = load(f)

        total_legislation = get_legislation_count(session)

        print(session)

        with tqdm(total=total_legislation) as progress_bar:
            for category in legislative_texts.keys():
                for legislation in legislative_texts[category]:
                    score = vader_model(legislation["text"])["compound"]
                    compound_all += score
                    count += 1
                    progress_bar.update()

        compound_average: float = compound_all / score

        print(compound_average)

        data[session] = compound_average

    print(data)

    # num_117 = testing(117)
    # num_116 = testing(116)
    # num_115 = testing(115)
    # num_114 = testing(114)

    # data = {"117": num_117, "116": num_116, "115": num_115, "114": num_114}

    # sessions = list(data.keys())
    # nums = list(data.values())

    # fig = plt.figure(figsize=(10, 5))

    # # creating the bar plot
    # plt.bar(sessions, nums, color="maroon", width=0.4)

    # plt.xlabel("Congressional Sessions")
    # plt.ylabel("No. of legislation")
    # plt.title("The number of legislation per congressional sessions.")

    # plt.show()


def get_sentiment_str(compound: float) -> str:
    if compound >= 0.05:
        return "positive"
    elif compound <= -0.05:
        return "negative"
    else:
        return "neutral"


if __name__ == "__main__":
    main()
    # general_score_average_checker("control", 117)
    # general_score_average_checker("rights", 117)

    # general_score_average_checker("control", 116)
    # general_score_average_checker("rights", 116)

    create_graph()
