# Scraper for IBDP pages on savemyexams.com (Biology, Chemistry, Physics, Math AA, Economics).

# IMPORTANT:
#  - Adjust the user-agent or request headers if needed.
#  - Inspect the site structure; you may need to handle multiple pages,
#    embedded JavaScript, or dynamic loading.
#  - Use additional libraries like Selenium if standard requests+BeautifulSoup
#    is insufficient.

import requests
from bs4 import BeautifulSoup
import os
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")


def scrape_savemyexams(base_url, subject_output_dir):
    os.makedirs(subject_output_dir, exist_ok=True)
    driver = webdriver.Chrome(options=options)
    driver.get(base_url)
    time.sleep(4)
    response = driver.page_source

    soup = BeautifulSoup(response, "html.parser")

    revision_sections = soup.select("div", class_="output")
    for section in revision_sections:
        ul = section.find("ul")
        if not ul:
            print("No list found in section")
            continue
        li_list = ul.find_all("li")
        for li in li_list:
            a_tag = li.find("a")
            if a_tag:
                link = a_tag.get("href")
                title = a_tag.text.strip()
                print("Downloading:", title, link)
                download_link = link
                download_file(download_link, subject_output_dir)
            else:
                print("No link found in list item")


def download_file(url, output_dir):
    # Download the file from the URL and save it locally under `output_dir` using the last part of the URL.
    # If the file already exists, skip downloading.
    filename = url.split("/")[-1]
    output_path = os.path.join(output_dir, filename)
    if os.path.exists(output_path):
        print(f"File already exists: {filename}")
        return
    with open(output_path, "wb") as f:
        browser = webdriver.Chrome(options=options)
        time.sleep(1)
        browser.get(url)
        time.sleep(2)
        response = browser.page_source
        f.write(response.encode("utf-8"))
    print(f"Downloaded: {filename}")
    time.sleep(1)  # Be polite and don't spam requests
