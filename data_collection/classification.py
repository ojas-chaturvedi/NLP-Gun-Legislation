#!/opt/homebrew/bin/python3
"""
Name: data_collection/classification.py
Purpose: To classify each Congressional legislation as pro-gun rights or pro-gun control using the OpenAI ChatGPT LLM
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from os import getenv
from dotenv import load_dotenv
from openai import OpenAI


def classification(legislative_text: str) -> str:
    load_dotenv()
    client = OpenAI(
        organization=f'{getenv('OPENAI_ORG_KEY')}',
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a legislative text regarding firearms, and your task is to classify it as pro-control or pro-rights. Your response can be one of two things: 'control' or 'rights'."
            },
            {
                "role": "user",
                "content": f"{legislative_text}"
            }
        ],
        temperature=0.0, # Also try 0.7 and 2.0 and check for different results
        top_p=1
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    # Test text
    text = "To prohibit Federal funding of State firearm ownership databases, and for other purposes. Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled, SECTION 1. SHORT TITLE. This Act may be cited as the ``Gun Owner Registration Information Protection Act''. SEC. 2. PROHIBITION ON FEDERAL FUNDING OF STATE FIREARM OWNERSHIP DATABASES. (a) Definitions.--In this section: (1) State.--The term ``State'' means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the Commonwealth of the Northern Mariana Islands, American Samoa, Guam, the United States Virgin Islands, and any other territory or possession of the United States. (2) State firearm ownership database.--The term ``State firearm ownership database'' means a comprehensive or partial database of a State or political subdivision of a State that lists-- (A) firearms lawfully owned or possessed by individuals; or (B) individuals who lawfully own or possess firearms. (b) Prohibition.--A Federal agency may not fund or otherwise support the establishment or maintenance of a State firearm ownership database. (c) Exception.--Subsection (b) shall not apply to a database of a State or political subdivision of a State that lists-- (1) firearms that have been reported as lost or stolen; or (2) individuals who have reported their firearms as lost or stolen."
    print(classification(text))
