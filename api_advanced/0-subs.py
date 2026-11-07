#!/usr/bin/python3
"""Module for querying Reddit subreddit subscribers."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "ALU student Reddit API project"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code != 200:
            return 0

        return response.json().get("data", {}).get("subscribers", 0)

    except (requests.RequestException, ValueError, TypeError):
        return 0
