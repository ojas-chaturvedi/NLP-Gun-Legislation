#!/opt/homebrew/bin/python3
"""
Name: sentiment_analysis/textblob_model.py
Purpose: To run legislative text through the TextBlob Sentiment Analysis Model


Model Name: TextBlob
Type: Rule-based model
Github link: https://github.com/sloria/TextBlob
Citation:

"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from textblob import TextBlob


def textblob_model(text: str) -> dict:
    """Get sentiment dictionary (containing pos, neg, neu, and compound scores)

    Args:
        text (str): Legislative text that will be run through the VADER sentiment analysis model

    Returns:
        dict: Dictionary of legislative text sentiment scores
    """

    analyzer = TextBlob(text)

    return analyzer.sentiment


if __name__ == "__main__":
    # Test text
    text = "To prohibit Federal funding of State firearm ownership databases, and for other purposes. Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled, SECTION 1. SHORT TITLE. This Act may be cited as the ``Gun Owner Registration Information Protection Act''. SEC. 2. PROHIBITION ON FEDERAL FUNDING OF STATE FIREARM OWNERSHIP DATABASES. (a) Definitions.--In this section: (1) State.--The term ``State'' means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the Commonwealth of the Northern Mariana Islands, American Samoa, Guam, the United States Virgin Islands, and any other territory or possession of the United States. (2) State firearm ownership database.--The term ``State firearm ownership database'' means a comprehensive or partial database of a State or political subdivision of a State that lists-- (A) firearms lawfully owned or possessed by individuals; or (B) individuals who lawfully own or possess firearms. (b) Prohibition.--A Federal agency may not fund or otherwise support the establishment or maintenance of a State firearm ownership database. (c) Exception.--Subsection (b) shall not apply to a database of a State or political subdivision of a State that lists-- (1) firearms that have been reported as lost or stolen; or (2) individuals who have reported their firearms as lost or stolen."

    print(textblob_model(text))
