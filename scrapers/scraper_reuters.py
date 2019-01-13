#!/usr/bin/env python

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import re
import csv
from urllib.parse import urljoin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# # source = requests.get("https://in.reuters.com/theWire").text
# # soup = BeautifulSoup(source,"lxml")
article_re = re.compile(".*article.*")
reporter_re = re.compile("Reporting by (\w+\s\w+)")
location_re = re.compile("(.*)\(Reuters\)")
base_url = "https://in.reuters.com/theWire"
def updateCsv(driver):
    website = driver.page_source
    soup = BeautifulSoup(website)
    articles = soup.findAll("article", {"class": article_re} )
    article_info = []
    for article in articles:
        article_url = article.find("a").get("href")
        article_title = " ".join(article.text.split(" ")[1:])[3:]
        for i in range(3):
            try:
                article_url_joined = urljoin(base_url, article_url)
                article_page = requests.get(article_url_joined).text
                break
            except:
                continue
        else:
            print("Skipping could not load")
            continue

        article_page_soup = BeautifulSoup(article_page, "lxml")
        article_text = ""
        for para in article_page_soup.findAll("p"):
            article_text+=para.text
        # article_location = article_text.split(" ")[2][4:]
        article_location = location_re.search(article_text)
        if(article_location is None or article_location is ""):
            article_location = "NaN NaN"
        else:
            article_location = article_location.group(1)
            article_location = " ".join(article_location.split(" ")[2:])[4:]

        article_text= " ".join(article_text.split(" ")[5:])
        article_journalist = reporter_re.search(article_text)
        if(article_journalist is None):
            article_journalist = "NaN NaN"
        else:
            article_journalist = article_journalist.group(1)
        article_date = article_page_soup.find("div",class_="ArticleHeader_date")
        if(article_date is None):
            article_date = "NaN NaN"
        else:
            article_date = article_date.text
        print(article_journalist)
        print(article_title)
        print(article_text)
        print(article_location)
        print(article_date)
        print(article_url)
        article_info.append([article_title, article_text, article_location, article_date, article_journalist, article_url_joined])
    with open("temp.csv", "a") as csvFile:
         csvWriter = csv.writer(csvFile)
         for row in article_info:
             csvWriter.writerow(row)
             csvFile.flush()
    with open('site.html',"w") as site:
        site.write(website)
        site.flush()

driver = webdriver.Firefox()
driver.get(base_url)
broken = False

for i in range(2000):
    for j in range(5):
        load_more_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "more-load")))
        load_more_button.click()
        break
    print("{}/2000 Loading more...".format(i))
updateCsv(driver)
with open('site.html',"w") as site:
        site.write(driver.page_source)
        site.flush()
