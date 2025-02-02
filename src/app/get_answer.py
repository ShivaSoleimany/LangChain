import streamlit as st
from typing import Any, Dict
import logging

from langchain.chains import RetrievalQAWithSourcesChain
from scripts.vectorstore import load_vectorstore
from app.llm import get_llm


@st.cache_data()
def get_answer(query:str, vectorstore_path:str, embedding_type:str="openai") :
    """
    Retrieves relevant documents from a FAISS vector store and generates an answer using an LLM.

    Args:
        query: The user's question to retrieve relevant information.
        vectorstore_path: Path to the FAISS index directory.
        embedding_type: Embedding model to use. "huggingface" or "openai".

    Returns:
        The output of the RetrievalQAWithSourcesChain, typically a dictionary with:
            - "answer" (str): The generated answer from the LLM.
            - "sources" (str): The source documents used to generate the answer.
    """
    try:
        vectorstore = load_vectorstore(vectorstore_path, embedding_type)
        llm = get_llm()

        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())

        return chain({"question": query}, return_only_outputs=True)

    except Exception as e:
        st.error(f"Error retrieving answer: {e}")
        return {"answer": None, "sources": None}