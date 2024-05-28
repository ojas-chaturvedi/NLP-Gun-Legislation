#!/opt/homebrew/bin/python3
"""
Name: src/data_collection/classification.py
Purpose: To classify each Congressional legislation as pro-gun rights or pro-gun control using the OpenAI ChatGPT LLM
"""

# Save the OpenAI API and Organization keys manually in a .env file at directory of file run

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"


import re
from os import getenv
from time import sleep

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError
from tiktoken import encoding_for_model


def classification(legislative_text: str) -> str:
    load_dotenv()
    client = OpenAI(
        organization=f'{getenv('OPENAI_ORG_KEY')}',
    )

    # Check if the legislative text is too large before sending it to the API.
    if calculate_tokens(legislative_text) > 128000:
        return "large"

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You will be provided with a legislative text regarding firearms, and your task is to classify it as pro-control or pro-rights. Your response can be one of two things: 'control' or 'rights'. Remember, I do not want a summary or anything. I just want a classification of the legislation.",
                },
                {"role": "user", "content": legislative_text},
            ],
            temperature=0.0,  # Also try 0.7 and 2.0 and check for different results
            top_p=1,
        )

        return response.choices[0].message.content.lower()

    except RateLimitError as e:
        match = re.search(r"Please try again in (\d+m)?(\d+s)?", str(e))
        if match:
            minutes = int(match.group(1)[:-1]) if match.group(1) else 0
            seconds = int(match.group(2)[:-1]) if match.group(2) else 0
            wait_time = minutes * 60 + seconds
            print(
                f"Rate limit reached, waiting for {minutes} minutes and {seconds} seconds."
            )
        else:
            wait_time = 60
            print(
                f"Rate limit reached, unable to parse retry time. Waiting for {wait_time} seconds."
            )
        sleep(wait_time)
        return classification(legislative_text)  # Retry after waiting
    except Exception as e:
        # Handle other exceptions that might occur
        print(f"An error occurred: {e}")
        return "error"


def calculate_tokens(text: str) -> int:
    """
    Get the number of tokens in the given text.
    """
    encoding = encoding_for_model("gpt-4")
    num_tokens = len(encoding.encode(text))

    return num_tokens


if __name__ == "__main__":
    # Test text
    text = "To prohibit Federal funding of State firearm ownership databases, and for other purposes. Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled, SECTION 1. SHORT TITLE. This Act may be cited as the ``Gun Owner Registration Information Protection Act''. SEC. 2. PROHIBITION ON FEDERAL FUNDING OF STATE FIREARM OWNERSHIP DATABASES. (a) Definitions.--In this section: (1) State.--The term ``State'' means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the Commonwealth of the Northern Mariana Islands, American Samoa, Guam, the United States Virgin Islands, and any other territory or possession of the United States. (2) State firearm ownership database.--The term ``State firearm ownership database'' means a comprehensive or partial database of a State or political subdivision of a State that lists-- (A) firearms lawfully owned or possessed by individuals; or (B) individuals who lawfully own or possess firearms. (b) Prohibition.--A Federal agency may not fund or otherwise support the establishment or maintenance of a State firearm ownership database. (c) Exception.--Subsection (b) shall not apply to a database of a State or political subdivision of a State that lists-- (1) firearms that have been reported as lost or stolen; or (2) individuals who have reported their firearms as lost or stolen."
    print(classification(text))
