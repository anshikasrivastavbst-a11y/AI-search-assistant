def build_web_content(search_results):

    web_content = ""

    for result in search_results["results"]:

        web_content += f"""
Title: {result['title']}
Content: {result['content']}
Source: {result['url']}

"""

    return web_content