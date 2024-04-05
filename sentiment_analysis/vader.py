#!/opt/homebrew/bin/python3
"""
Name: sentiment_analysis/vader.py
Purpose: To run legislative text through the VADER Sentiment Analysis Model


Model Name: VADER (Valence Aware Dictionary and sEntiment Reasoner)
Github link: https://github.com/cjhutto/vaderSentiment
Citation:
    Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

if __name__ == "__main__":
    # Test text
    text = "To prohibit Federal funding of State firearm ownership databases, and for other purposes. Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled, SECTION 1. SHORT TITLE. This Act may be cited as the ``Gun Owner Registration Information Protection Act''. SEC. 2. PROHIBITION ON FEDERAL FUNDING OF STATE FIREARM OWNERSHIP DATABASES. (a) Definitions.--In this section: (1) State.--The term ``State'' means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the Commonwealth of the Northern Mariana Islands, American Samoa, Guam, the United States Virgin Islands, and any other territory or possession of the United States. (2) State firearm ownership database.--The term ``State firearm ownership database'' means a comprehensive or partial database of a State or political subdivision of a State that lists-- (A) firearms lawfully owned or possessed by individuals; or (B) individuals who lawfully own or possess firearms. (b) Prohibition.--A Federal agency may not fund or otherwise support the establishment or maintenance of a State firearm ownership database. (c) Exception.--Subsection (b) shall not apply to a database of a State or political subdivision of a State that lists-- (1) firearms that have been reported as lost or stolen; or (2) individuals who have reported their firearms as lost or stolen."

    print(vader(text))
