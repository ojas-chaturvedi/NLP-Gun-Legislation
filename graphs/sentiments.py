#!/opt/homebrew/bin/python3
"""
Name: graphs/sentiments.py
Purpose: To create csv files for graphs with the sentiment scores and other factors
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"


from csv import DictReader, writer
from datetime import datetime

from sentiment_analysis.initialize import session_end, session_start

sentimentVStime = {}
control = []
rights = []

for session in range(session_start, session_end + 1):
    csvFile = DictReader(open(f"sentiment_analysis/data/{session}.csv", "r"))

    for legislation in csvFile:
        date = datetime.strptime(legislation["Date of Introduction"], "%m/%d/%Y")

        sentiment = float(legislation["VADER Sentiment Score"])

        if date not in sentimentVStime:
            sentimentVStime[date] = []

        sentimentVStime[date].append(sentiment)

        if legislation["Classification"] == "control":
            control.append(sentiment)
        else:
            rights.append(sentiment)

sentimentVStime = dict(sorted(sentimentVStime.items()))

with open("graphs/overall.csv", "w") as file:
    write = writer(file)

    headers = [
        "Date of Introduction",
        "Sentiment Score",
    ]

    write.writerow(headers)

    for date, sentiments in sentimentVStime.items():
        for value in sentiments:
            date_new = f"{date.strftime("%m")}/{date.strftime("%d")}/{date.strftime("%Y")}"
            data = [date_new, value]

            write.writerow(data)

with open("graphs/control_histogram.csv", "w") as file:
    write = writer(file)

    headers = ["Pro-Control Legislation Sentiment Values"]

    write.writerow(headers)

    for value in control:
        data = [value]
        write.writerow(data)

with open("graphs/rights_histogram.csv", "w") as file:
    write = writer(file)

    headers = ["Pro-Rights Legislation Sentiment Values"]

    write.writerow(headers)

    for value in rights:
        data = [value]
        write.writerow(data)
