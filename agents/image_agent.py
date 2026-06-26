import requests


def search_images(query, api_key):
    """
    Search for related images using Tavily.
    """

    url = "https://api.tavily.com/search"

    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "basic",
        "include_images": True,
        "max_results": 5
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    print(data)

    return data