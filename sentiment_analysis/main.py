#!/opt/homebrew/bin/python3
"""
Name: sentiment_analysis/main.py
Purpose: To run the sentiment analysis models and generate results / graphs
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from csv import field_size_limit, reader, writer
from json import load
from sys import maxsize

from tqdm import tqdm

from sentiment_analysis.initialize import session_end, session_start
from sentiment_analysis.textblob_model import textblob_model
from sentiment_analysis.vader_model import vader_model

field_size_limit(maxsize)


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
        "VADER": vader_model,
        "TextBlob": textblob_model,
    }

    sentiment_function = model_functions.get(model)

    with open(f"data_collection/data/{session}.csv", "r") as f:
        read = reader(f)
        legislative_data = list(read)

    with open(f"sentiment_analysis/data/{session}.csv", "r") as f:
        read = reader(f)
        data = list(read)

    data[0].append(f"{model} Sentiment Score")

    with tqdm(total=len(data)) as progress_bar:
        for i in range(1, len(data)):
            name = data[i][0]
            for legislation in legislative_data:
                if name == legislation[0]:
                    text = legislation[7]
            sentiment = sentiment_function(text)
            data[i].append(sentiment)
            progress_bar.update(1)

    with open(f"sentiment_analysis/data/{session}.csv", "w") as f:
        write = writer(f)
        write.writerows(data)


if __name__ == "__main__":
    # Remember to run sentiment_analysis/initialize.py first before saving sentiment analysis model scores to JSON files

    for session in range(session_start, session_end + 1):
        print("-" * 30)
        print(f"Session {session}")
        save_data(session, "VADER")
        save_data(session, "TextBlob")
