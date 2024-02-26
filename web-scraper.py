#!/opt/homebrew/bin/python3
"""
Web Scraper to receive legislation from Congress.gov
"""

__author__ = "Ojas Chaturvedi"
__github__ = "ojas-chaturvedi"
__license__ = "MIT"

from selenium import webdriver
from bs4 import BeautifulSoup

def main(url):
    """ Main entry point of the file """

    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    driver.close()

    doc = BeautifulSoup(html, "html.parser")

    # print(doc.prettify())

    tag = doc.pre
    print(tag.prettify())
    # print(tag.type)
    # tag_list = tag.split()

    # with open("web-scraper-testing.html", "w") as f:
    #     for i in tag_list:
    #         f.write(i)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main('https://www.congress.gov/bill/117th-congress/house-bill/7544/text?format=txt')
