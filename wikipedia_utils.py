import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='YourAppName/1.0 (https://yourappurl.com; your@email.com)'
)

def get_wikipedia_page(title):
    page = wiki_wiki.page(title)
    return page.text if page.exists() else None
