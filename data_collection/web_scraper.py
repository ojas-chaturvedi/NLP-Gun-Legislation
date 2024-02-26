#!/opt/homebrew/bin/python3
"""
Web Scraper to receive legislation from Congress.gov
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"

from selenium import webdriver
from bs4 import BeautifulSoup


def web_scraper(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    driver.close()

    doc = BeautifulSoup(html, "html.parser")
    tag = doc.pre
    text = tag.string

    text_list = text.split()

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

    text_join = " ".join(text_list)
    print(text_join)


if __name__ == "__main__":
    # Test url
    web_scraper("https://www.congress.gov/bill/117th-congress/house-bill/7544/text?format=txt")
