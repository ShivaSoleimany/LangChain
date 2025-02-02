from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List


def chunk_text(text: str, chunk_size: int = 400, overlap: int = 50):
    """
    Splits text into overlapping chunks for better retrieval.

    Args:
        text (str): The input text to be chunked.
        chunk_size: The size of each chunk. Default is 500.
        overlap: The overlap between consecutive chunks. Default is 50.

    Returns:
        List[str]: A list of text chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )

    return splitter.split_documents(text)