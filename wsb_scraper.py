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



def scrape_wsb():
    chromedriver = os.getcwd() + "/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    #driver = webdriver.Chrome(chromedriver)
    #driver.get("https://newyork.craigslist.org/d/resumes/search/rrr")

    options = Options()
    options.headless = True
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chromedriver, chrome_options=options)

    links = []

    URL = "https://old.reddit.com/r/wallstreetbets/"
    page = requests.get(URL)

    #print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)

if __name__ == "__main__":
    scrape_wsb()