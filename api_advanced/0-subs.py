#!/usr/bin/python3
"""Return the number of subscribers for a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subreddit subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALU-RedditAPI/1.0"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code != 200:
            return 0

        data = response.json()
        return data["data"]["subscribers"]

    except (requests.RequestException, ValueError, KeyError, TypeError):
        return 0

