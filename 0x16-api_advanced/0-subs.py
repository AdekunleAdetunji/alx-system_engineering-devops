#!/usr/bin/python3
"""
This module contains a function used to obtain the number of subscribers
in a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subreddit subscriber
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "hshdl"}
    resObj = requests.get(url=url, headers=headers, allow_redirects=False)
    if resObj.status_code != 200:
        return 0
    json = resObj.json()
    return (json.get("data").get("subscribers"))
