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


def save_data(session: int, model: str) -> None:
    model_functions = {
        "vader": vader_model,
        "textblob": textblob_model,
    }

    with open(f"sentiment_analysis/data/{session}.json", "r") as f:
        legislative_sentiments = load(f)
    with open(f"data_collection/data/{session}.json", "r") as f:
        legislative_texts = load(f)

    total_legislation: int = sum(
        len(legislation) for legislation in legislative_sentiments.values()
    )

    with tqdm(total=total_legislation) as progress_bar:
        for category in legislative_sentiments.keys():
            for legislation in legislative_sentiments[category]:

                name = legislation["name"]
                for legislation_text in legislative_texts[category]:
                    if name == legislation_text["name"]:
                        text = legislation_text["text"]

                sentiment_function = model_functions.get(model)
                sentiment = sentiment_function(text)

                legislation[model] = sentiment
                progress_bar.update(1)

    with open(f"sentiment_analysis/data/{session}.json", "w") as file:
        dump(legislative_sentiments, file, indent=4)


if __name__ == "__main__":
    # Remember to run sentiment_analysis/initialize.py first before saving sentiment analysis model scores to JSON files

    session_start = 107
    session_end = 117

    for session in range(session_start, session_end + 1):
        print("-" * 30)
        print(f"Session {session}")
        save_data(session, "vader")
        save_data(session, "textblob")
