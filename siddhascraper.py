#!/usr/bin/env python3 

import urllib.request 
from bs4 import BeautifulSoup
import sys 
import os 
import re

def scrape(url):
    req = urllib.request.Request(
        url, 
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    try: 
        html = urllib.request.urlopen(req)
    except HTTPError as e: 
        print(e)
        return None
    except URLError: 
        print("The server could not be found!")

    # get title of discourse 
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('a', href=re.compile(f'^{url}.*$')).text
    title = title.replace(' ', '-').lower()

    # get body text 
    body = bs.find_all('p')

    # read discourse body into txt file 
    for p in body:
        line = p.get_text()
        if line == "Kapil Gupta is a personal advisor to Kings, Queens, CEO’s, Professional Athletes, Celebrities, and Performing Artists around the world.":
            return
        else:
            os.system(f'echo {line} >> {title}.txt')

url = sys.argv[1]
scrape(url)
