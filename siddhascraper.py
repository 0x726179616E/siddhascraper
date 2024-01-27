#!/usr/bin/env python3 

import urllib.request 
import urllib.error 
from bs4 import BeautifulSoup
import sys 
import os 
import re

# takes in a url and echoes the remote text to a local .txt file 
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
    except urllib.error.HTTPError as e: 
        print(e)
        return None
    except urllib.error.URLError: 
        print("The server could not be found.")

    # create directory to store discourses
    dir_name = "discourses"
    if not os.path.isdir(dir_name): os.makedirs(dir_name)

    # get title of discourse 
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('a', href=re.compile(f'^{url}.*$')).text
    title = title.replace(' ', '-').lower()

    # get body text 
    body = bs.find_all('p')

    # read discourse body into txt file 
    for p in body:
        line = p.get_text()
        if line == "Kapil Gupta is a personal advisor to Kings, Queens, CEO’s, Professional Athletes, Celebrities, and Performing Artists around the world.": return 0
        else: os.system(f'echo {line} >> ./{dir_name}/{title}.txt')
    return -1
    

# driver function
if __name__ == "__main__":
    print()
    if len(sys.argv) < 2:
        print("Insufficient command-line arguments.")
        print("Correct usage: ./siddhascraper <ARTICLE_URL> <OPTIONALLY_ADDITIONAL_ARTICLE_URLS> <...>")
        exit(1)
    for arg in sys.argv[1:]:
        path = scrape(arg)
        if path == 0: print(f"Successfully scraped: {arg}\n")
        else: print(f"Error scraping: {arg}\n")
    print("All done.")
    print()
    exit(0)