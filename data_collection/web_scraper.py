#!/opt/homebrew/bin/python3
"""
Web Scraper to receive legislation from Congress.gov
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"

from selenium import webdriver
from bs4 import BeautifulSoup
import time


def web_scraper(url):
    # Simulate chrome site with url, wait for it to load, and grab the html source code
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    driver.close()

    # Parse the html code, find relevant <pre></pre> tag with string for legislation text, and split it into a list
    doc = BeautifulSoup(html, "html.parser")
    tag = doc.pre
    text = tag.string
    text_list = text.split()

    # Find the second line break and remove useless information before it (header and signatories)
    count = 0
    occurrence = 2
    index = 0
    for i in range(len(text_list)):
        if (
            text_list[i]
            == "_______________________________________________________________________"
        ):
            count += 1
            if count == occurrence:
                index = i
    del text_list[: index + 1]
    del text_list[-1]

    # Join the modified list into a string and print
    text_join = " ".join(text_list)
    print(text_join)


if __name__ == "__main__":
    # Test url
    web_scraper(
        "https://www.congress.gov/bill/117th-congress/house-resolution/437/text?format=txt"
    )
