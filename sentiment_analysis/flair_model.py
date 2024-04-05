#!/opt/homebrew/bin/python3
"""
Name: sentiment_analysis/flair_model.py
Purpose: To run legislative text through the Flair Sentiment Analysis Model


Model Name: Flair
Type: Rule-based model
Github link: https://github.com/flairNLP/flair
Citation:
    @inproceedings{akbik2019flair,
        title={{FLAIR}: An easy-to-use framework for state-of-the-art {NLP}},
        author={Akbik, Alan and Bergmann, Tanja and Blythe, Duncan and Rasul, Kashif and Schweter, Stefan and Vollgraf, Roland},
        booktitle={{NAACL} 2019, 2019 Annual Conference of the North American Chapter of the Association for Computational Linguistics (Demonstrations)},
        pages={54--59},
        year={2019}
    }
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from flair.data import Sentence
from flair.models import TextClassifier


def flair_model(text: str) -> float:
    """Get sentiment dictionary (containing pos, neg, neu, and compound scores)

    Args:
        text (str): Legislative text that will be run through the flair sentiment analysis model

    Returns:
        float: Overall sentiment score of legislative text
    """

    text = Sentence(text)

    classifier = TextClassifier.load('en-sentiment')
    classifier.predict(text)

    score = text.labels[0].score

    if text.labels[0].value == "NEGATIVE":
        score *= -1

    return score


if __name__ == "__main__":
    # Test text
    text = "To prohibit Federal funding of State firearm ownership databases, and for other purposes. Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled, SECTION 1. SHORT TITLE. This Act may be cited as the ``Gun Owner Registration Information Protection Act''. SEC. 2. PROHIBITION ON FEDERAL FUNDING OF STATE FIREARM OWNERSHIP DATABASES. (a) Definitions.--In this section: (1) State.--The term ``State'' means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the Commonwealth of the Northern Mariana Islands, American Samoa, Guam, the United States Virgin Islands, and any other territory or possession of the United States. (2) State firearm ownership database.--The term ``State firearm ownership database'' means a comprehensive or partial database of a State or political subdivision of a State that lists-- (A) firearms lawfully owned or possessed by individuals; or (B) individuals who lawfully own or possess firearms. (b) Prohibition.--A Federal agency may not fund or otherwise support the establishment or maintenance of a State firearm ownership database. (c) Exception.--Subsection (b) shall not apply to a database of a State or political subdivision of a State that lists-- (1) firearms that have been reported as lost or stolen; or (2) individuals who have reported their firearms as lost or stolen."

    print(flair_model(text))
