import os
import logging
import requests
import streamlit as st
# from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchResults


logging.basicConfig(level=logging.INFO)

def fetch_search_results(query):
    """
    Attempts to fetch URLs using DuckDuckGo first, then falls back to SerpAPI.
    """
    urls = fetch_search_results_ddg(query)
    if not urls:
        logging.warning("DuckDuckGo returned no results. Falling back to SerpAPI.")
        urls = fetch_search_results_serpapi(query)
    return urls

def fetch_search_results_serpapi(query, max_results=5):
    """
    Fetch URLs using SerpAPI and return relevant article links.
    """
    API_KEY = os.getenv("SERPAPI_KEY")
    if not API_KEY:
        logging.error("SERPAPI_KEY is missing. Please check your .env file.")
        st.error("Search API key is missing.")
        return []

    search_url = "https://serpapi.com/search"
    params = {
        "q": query,
        "hl": "en",
        "gl": "us",
        "num": max_results,
        "api_key": API_KEY
    }

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        results = response.json()

        urls = [result.get("link") for result in results.get("organic_results", []) if "link" in result]

        if not urls:
            logging.warning("SerpAPI returned no relevant articles.")
            return []

        logging.info(f"Retrieved {len(urls)} URLs from SerpAPI.")
        return urls

    except requests.exceptions.RequestException as e:
        logging.error(f"SerpAPI request failed: {e}")
        st.error("Failed to fetch search results from SerpAPI.")
        return []

def fetch_search_results_ddg(query, max_results=5):
    """
    Fetch URLs using DuckDuckGo and return relevant article links.
    """
    try:

        wrapper = DuckDuckGoSearchAPIWrapper(time="d", max_results=max_results)
        results = wrapper.results(query, max_results=max_results)

        if not results:
            logging.warning("DuckDuckGo returned no results.")
            return []

        urls = [result.get("link") for result in results if "link" in result]
        logging.info(f"Retrieved {len(urls)} URLs from DuckDuckGo.")
        return urls

    except Exception as e:
        logging.error(f"DuckDuckGo request failed: {e}")
        return []



# import os
# import requests
# import logging

# def fetch_search_results(query):
#     """
#     Fetch URLs using SerpAPI and return relevant article links.
#     """
#     API_KEY = os.getenv("SERPAPI_KEY")
#     if not API_KEY:
#         logging.error("SERPAPI_KEY is missing. Please check your .env file.")
#         return []

#     search_url = "https://serpapi.com/search"
#     params = {
#         "q": query,
#         "hl": "en",
#         "gl": "us",
#         "num": 5,  # Number of results
#         "api_key": API_KEY
#     }

#     try:
#         response = requests.get(search_url, params=params)
#         response.raise_for_status()
#         results = response.json()
#         return [result["link"] for result in results.get("organic_results", [])]
    
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Error fetching search results: {e}")
#         return []


