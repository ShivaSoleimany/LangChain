import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print("Added to PYTHONPATH:", os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import logging
from scripts.search import fetch_search_results
from scripts.url_loader import load_web_documents
from scripts.chunker import chunk_text
from scripts.vectorstore import create_faiss_index, save_vectorstore
from app.get_answer import get_answer
from app.llm import get_embeddings


st.set_page_config(page_title="RockyBot: News Research Tool 📈", layout="centered")
st.title("Question Answering RAG")

embedding_type: str = st.selectbox("Choose Embedding Model", ["openai", "huggingface"])
file_path: str = "src/data/faiss_index"
query: str = st.text_input("Enter your question:")


def process_documents(query: str, embedding_type: str, file_path: str) -> None:

    """
    Fetches relevant articles, extracts content, chunks text, and stores embeddings in FAISS.

    Args:
        query (str): The user's search query.

        embedding_type (str): The embedding model type ("openai" or "huggingface").

        file_path (str): Path to save the FAISS index.
    """

    st.write("Fetching relevant articles...")
    urls: List[str] = fetch_search_results(query)

    if not urls:
        st.error("No articles found.")
        return

    st.write(f"Retrieved {len(urls)} URLs. Extracting content...")
    documents = load_web_documents(urls)
    st.write("Splitting documents into smaller chunks...")

    text_chunks = chunk_text(documents)

    logging.info(f"text_chunks:\n{text_chunks}")

    st.write("Embedding and indexing documents...")
    vectorstore = create_faiss_index(text_chunks, embedding_type)
    logging.info(f"Saving FAISS index at {file_path}")

    save_vectorstore(vectorstore, file_path)
    st.write("FAISS index saved successfully! 🚀")

def retrieve_answer(query: str, file_path: str, embedding_type: str) -> None:
    """
    Retrieves an answer from FAISS and LLM based on the query.

    Args:
        query (str): The user's search query.
        file_path (str): Path to the FAISS index.
        embedding_type (str): The embedding model type.
    """
    with st.spinner("Retrieving answer...⏳"):

        result = get_answer(query, file_path, embedding_type)

        st.header("Answer:")
        st.write(result.get("answer", "No answer found."))

        logging.info(result)

        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            for idx, source in enumerate(sources.strip().split("\n"), start=1):  # Fixed source formatting
                st.markdown(f"**{idx}.** [{source}]({source})")


if query:
    process_documents(query, embedding_type, file_path)
    retrieve_answer(query, file_path, embedding_type)