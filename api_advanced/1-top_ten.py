#!/usr/bin/python3
"""Module for retrieving the top ten hot Reddit posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "ALU student Reddit API project"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            print(post["data"]["title"])

    except (requests.RequestException, ValueError, KeyError, TypeError):
        print(None)
