#!/usr/bin/python3
"""Module for number_of_subscribers function"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
