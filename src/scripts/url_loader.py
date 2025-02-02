from langchain.schema import Document
from langchain.document_loaders import WebBaseLoader
from typing import List

def load_web_documents(urls: List[str]) -> List[Document]:
    """
    Fetches and loads text documents from a list of URLs.

    Args:
        urls (List[str]): A list of URLs to fetch content from.

    Returns:
        List[Document]: A list of LangChain Document objects containing the extracted text.

    Raises:
        ValueError: If `urls` is not a list or is empty.
    """

    if not isinstance(urls, list) or not all(isinstance(url, str) for url in urls):
        raise ValueError("Input must be a list of URLs (strings).")

    if not urls:
        return []  # Return empty list instead of calling WebBaseLoader with no URLs

    loader = WebBaseLoader(urls)

    try:
        return loader.load()
    except Exception as e:
        raise RuntimeError(f"Failed to load documents from URLs: {e}")