#!/usr/bin/python3
"""
This module contains a function used to obtain the top ten hot posts
in a subreddit
"""
import requests


def top_ten(subreddit):
    """
    print the top ten hot posts in a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "shdfs"}
    payload = {"limit": 10}
    resObj = requests.get(url=url, headers=headers,
                          params=payload, allow_redirects=False)
    if resObj.status_code != 200:
        return 0
    data = resObj.json().get("data").get("children")
    for datum in data:
        print(datum.get("data").get("title"))
