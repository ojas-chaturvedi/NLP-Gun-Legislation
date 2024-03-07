#!/opt/homebrew/bin/python3
"""
Name: data_collection/classification.py
Purpose: To classify each Congressional legislation as pro-gun rights or pro-gun control using the OpenAI ChatGPT LLM
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"

from os import getenv
from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    load_dotenv()
    client = OpenAI()


if __name__ == "__main__":
    main()
