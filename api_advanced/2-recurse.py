
#!/usr/bin/python3
"""Recursively retrieve all hot post titles."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list containing all hot post titles."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-RedditAPI/1.0"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            return None

        data = response.json()["data"]
        posts = data["children"]

        for post in posts:
            hot_list.append(post["data"]["title"])

        next_after = data["after"]

        if next_after is None:
            return hot_list if hot_list else None

        return recurse(subreddit, hot_list, next_after)

    except (requests.RequestException, ValueError, KeyError, TypeError):
        return None

