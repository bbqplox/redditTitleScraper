#!/usr/bin/python

from bs4 import BeautifulSoup
import requests

def main():
    url = raw_input("Enter a subreddit to see new topics: ")

    r = requests.get("http://reddit.com/r/" + url + "/new/")

    #print(url)

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    for title in soup.find_all('p', class_='title'):
        print(title.find_all(text=True))[0]

main()
