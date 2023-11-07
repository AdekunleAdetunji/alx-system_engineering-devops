#!/usr/bin/python3
"""
This module contains a recursive function that returns the list of all hot
articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """
    recursive function that returns a list of all hot articles linked to
    a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"user-agent": "hsld"}
    payload = {"after": after, "limit": 100, "count": count}
    response = requests.get(url, headers=headers,
                            params=payload, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data")
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    after = data.get("after")
    count += data.get("dist")

    if after:
        recurse(subreddit, hot_list, count, after)
    return hot_list
