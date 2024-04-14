#!/opt/homebrew/bin/python3
"""
Name: graphs/parties.py
Purpose: To create data for a bar graph showing # of pro-control and pro-rights legislation per political party
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from csv import DictReader, writer

from sentiment_analysis.initialize import session_end, session_start

control = {
    "democratic": 0,
    "republican": 0,
}
rights = {
    "democratic": 0,
    "republican": 0,
}

for session in range(session_start, session_end + 1):
    csvFile = DictReader(open(f"sentiment_analysis/data/{session}.csv", "r"))

    for legislation in csvFile:
        if legislation["Party of Sponsors"] == "Republican":
            if legislation["Classification"] == "control":
                control["republican"] += 1
            else:
                rights["republican"] += 1
        else:
            if legislation["Classification"] == "control":
                control["democratic"] += 1
            else:
                rights["democratic"] += 1

with open("graphs/parties.csv", "w") as file:
    write = writer(file)

    headers = [
        "",
        "Pro-Control",
        "Pro-Rights",
    ]

    democratic = ["Democratic", control["democratic"], rights["democratic"]]
    republican = ["Republican", control["republican"], rights["republican"]]

    write.writerow(headers)
    write.writerow(democratic)
    write.writerow(republican)
