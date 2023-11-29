#! /bin/env python3

import json
import requests
from bs4 import BeautifulSoup
import webbrowser


def scrape_python_urls(topic_url):
    # send a HTTP request 
    response = requests.get(topic_url)

    # check if the resquet work
    if response.status_code != 200:
        print("request failled: ", response.status_code)
        return []
    else:
        urls = []
        # Analyse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # find all link
        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            if href and 'http' in href:  # check if it's a true url
                urls.append(href)
        return urls



topic_url = "https://www.alice.org/resources/exercise-and-project/tutorial-control-structures-loops/" #put your own 
urls = scrape_python_urls(topic_url)

print(urls)









