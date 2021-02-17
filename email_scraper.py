import time
import requests
import os
import datetime
import heapq
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



def scrape_craiglist():
    chromedriver = os.getcwd() + "/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(chromedriver, chrome_options=options)

    links = []

    URL = "https://newyork.craigslist.org/d/resumes/search/rrr"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='searchform')
    job_elems = results.find_all('li', class_='result-row')

    total_amt = 500
    i = 0

    for job_elem in job_elems:
        link = job_elem.find('a')['href']
        links.append(link)
        if i > total_amt:
            break
        i += 1

    file1 = open("test_emails.txt","w+") 

    for link in links:
        driver.get(link)

        button_field = driver.find_element_by_css_selector("button[role='button'][class='reply-button js-only']").click()

        time.sleep(3)
        htmlSource = driver.page_source

        soupL = BeautifulSoup(htmlSource, 'html.parser')
        results2 = soupL.findAll('input', class_='anonemail')
        output = results2[0]['value']
        file1.write(output)
        file1.write("\n")

    file1.close()

if __name__ == "__main__":
    scrape_craiglist()