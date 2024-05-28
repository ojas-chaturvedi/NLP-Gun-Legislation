#!/opt/homebrew/bin/python3
"""
Name: src/data_collection/scraper.py
Purpose: To scrape the Congress.gov website to receive legislation data
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def web_scraper(url: str) -> str:
    # Modify url to access text page
    url += "/text?format=txt"

    # Simulate Chrome browser to retrieve HTML source code
    driver = webdriver.Chrome()
    driver.get(url)

    # Explicitly wait for the <pre> tag to be available, otherwise return error as text
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "pre"))
        )
    except TimeoutException:
        return "ERROR: TXT file does not exist; Check link manually."

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

    # Remove starting word(s) that describe the type of legislation
    # Check if the first few words indicate a type of legislation and remove them accordingly
    start_words = ["A BILL", "RESOLUTION", "JOINT RESOLUTION", "CONCURRENT RESOLUTION"]
    for start_word in start_words:
        if text_list[: len(start_word.split())] == start_word.split():
            del text_list[: len(start_word.split())]

    # Join the modified list into a string and return
    modified_text = " ".join(text_list)
    return modified_text


if __name__ == "__main__":
    # Test URLs
    urls = [
        "https://www.congress.gov/bill/117th-congress/house-bill/7544",
        "https://www.congress.gov/bill/117th-congress/house-resolution/437",
        "https://www.congress.gov/bill/115th-congress/house-bill/3249",
        "https://www.congress.gov/bill/117th-congress/senate-joint-resolution/49",
        "https://www.congress.gov/bill/116th-congress/house-concurrent-resolution/46",
    ]

    for url in urls:
        print(web_scraper(url))
