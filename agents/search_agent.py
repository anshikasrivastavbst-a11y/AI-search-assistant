from tavily import TavilyClient

def search_web(query, api_key):

    tavily = TavilyClient(api_key=api_key)

    results = tavily.search(
        query=query,
        max_results=5
    )

    return results