#!/usr/bin/python3
"""
This module contains a recursive function that returns the list of all hot
articles for a given subreddit
"""
import requests


def count_words(subreddit, word_list, after="", dic={}):
    """
    recursive function that returns frequency of certain words in all titles of
    articles linked to a subreddit
    """
    word_list = set([word.lower() for word in word_list])
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"user-agent": "shdh"}
    payload = {"after": after}
    response = requests.get(url, headers=headers,
                            params=payload, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data")
    for child in data.get("children"):
        title_words = child.get("data").get("title").lower().split()
        for word in word_list:
            dic[word] = dic.get(word, 0) + title_words.count(word)
    after = data.get("after")

    if after:
        count_words(subreddit, word_list, after, dic)

    else:
        word_list.sort(key=lambda x: dic.get(x), reverse=True)
        for word in word_list:
            if dic.get(word):
                print("{}: {}".format(word, dic.get(word)))
