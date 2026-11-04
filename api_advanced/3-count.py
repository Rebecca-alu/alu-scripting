
#!/usr/bin/python3
"""Count keyword occurrences in hot Reddit post titles."""

import requests


def count_words(subreddit, word_list):
    """Count and print keyword occurrences in hot post titles."""
    if not word_list:
        return

    headers = {"User-Agent": "ALU-RedditAPI/1.0"}
    word_counts = {}

    # Keep duplicate keywords so their counts are added together.
    for word in word_list:
        word = word.lower()
        word_counts[word] = word_counts.get(word, 0)

    def get_posts(after=None):
        """Recursively retrieve all hot post titles."""
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
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
                title_words = post["data"]["title"].lower().split()

                for word in word_counts:
                    occurrences = title_words.count(word)
                    word_counts[word] += occurrences * word_list.count(word)

            next_after = data["after"]

            if next_after is None:
                return True

            return get_posts(next_after)

        except (requests.RequestException, ValueError, KeyError, TypeError):
            return None

    result = get_posts()

    if result is None:
        return

    sorted_words = sorted(
        word_counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    for word, count in sorted_words:
        if count > 0:
            print("{}: {}".format(word, count))

