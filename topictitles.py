#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import threading

url = raw_input("Enter a subreddit: ")
key = raw_input("Enter substring: ")

#titleList = {}

def getTitles():
    r = requests.get("http://reddit.com/r/" + url + "/new/")

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    titleList = []

    for title in soup.find_all('p', class_='title'):
        #print(title.find_all(text=True))[0]
        pair = ((title.find_all(text=True))[0], False)
        titleList.append(pair)
        #titleList[(title.find_all(text=True))[0]] = False

    for place, temp in enumerate(titleList):
        (hit, read) = temp
        #print(str(hit))
        #print(read)
        if str(key) not in str(hit) or read is True:
            continue
        setTrue = (hit, True)
        titleList[place] = setTrue
        print(str(hit))
        #print(titleList[place][1])


    print("\n")

    threading.Timer(15, getTitles).start()

getTitles()
