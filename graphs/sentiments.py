#!/opt/homebrew/bin/python3
"""
Name: graphs/sentiments.py
Purpose: To make graphs with the sentiment scores and other factors
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"


from csv import DictReader, writer
from datetime import datetime

from sentiment_analysis.initialize import session_end, session_start

sentimentVStime = {}

for session in range(session_start, session_end + 1):
    csvFile = DictReader(open(f"sentiment_analysis/data/{session}.csv", "r"))

    for legislation in csvFile:
        date = datetime.strptime(legislation["Date of Introduction"], "%m/%d/%Y").date()
        sentiment = float(legislation["VADER Sentiment Score"])

        sentimentVStime[date] = sentiment

sentimentVStime = dict(sorted(sentimentVStime.items()))

with open("graphs/overall.csv", "w") as file:
    write = writer(file)

    headers = [
        "Date of Introduction",
        "Sentiment Score",
    ]

    write.writerow(headers)

    for date, sentiment in sentimentVStime.items():
        data = [date, sentiment]

        write.writerow(data)
