#!/opt/homebrew/bin/python3
"""
Web Scraper to receive legislation from Congress.gov
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"


from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def web_scraper(url):
    # Modify url to access text page
    url += "/text?format=txt"

    # Simulate Chrome browser to retrieve HTML source code
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(1)  # Wait for the page to load
    html = driver.page_source
    driver.close()

    # Parse HTML code to extract relevant legislation text
    doc = BeautifulSoup(html, "html.parser")
    tag = doc.pre
    text = tag.string

    # Split the text into a list of words
    text_list = text.split()

    # Find and remove header and signatories information before the legislation text
    count = 0
    occurrence = 2
    index = 0
    for i, word in enumerate(text_list):
        if (
            word
            == "_______________________________________________________________________"
        ):
            count += 1
            if count == occurrence:
                index = i
    del text_list[: index + 1]  # Remove header
    del text_list[-1]  # Remove trailing information

    # Join the modified list into a string and return
    modified_text = " ".join(text_list)
    return modified_text


if __name__ == "__main__":
    # Test url
    web_scraper(
        "https://www.congress.gov/bill/117th-congress/house-resolution/437",
    )
