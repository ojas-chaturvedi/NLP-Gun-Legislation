#!/opt/homebrew/bin/python3
"""
Name: sentiment_analysis/main.py
Purpose: To run the sentiment analysis models and generate results / graphs
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from json import dump, load

from tqdm import tqdm

from sentiment_analysis.textblob_model import textblob_model
from sentiment_analysis.vader_model import vader_model


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


def get_sentiment_str(compound: float) -> str:
    # Only works with VADER and TextBlob, not the HuggingFace models
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

