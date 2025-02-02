import logging
from typing import List
from langchain.vectorstores import FAISS
from langchain.schema import Document
from app.llm import get_embeddings

logging.basicConfig(level=logging.INFO)

def create_faiss_index(docs: List[Document], embedding_type: str="openai")-> FAISS:
    """
    Embeds text chunks and stores them in FAISS.

    Args:
        docs: A list of LangChain Document objects to embed.
        embedding_type: Embedding model to use ("openai" or "huggingface"). Default is "openai".

    Returns:
        FAISS: A FAISS vector store containing embedded documents.
    """
    embeddings = get_embeddings(embedding_type)
    return FAISS.from_documents(docs, embedding=embeddings)

def save_vectorstore(vectorstore: FAISS, path: str = "/data/faiss_index") -> None:
    """
    Saves FAISS index to disk.

    Args:
        vectorstore: The FAISS vector store to save.
        path: Path to save the FAISS index. Default is "data/faiss_index".

    Returns:
        None
    """
    logging.info(f"Saving FAISS index to {path}")
    vectorstore.save_local(path)


def load_vectorstore(path: str = "data/faiss_index", embedding_type: str = "openai") -> FAISS:
    """
    Loads FAISS index from disk.

    Args:
        path: Path to the FAISS index. Default is "data/faiss_index".
        embedding_type: Embedding model to use for loading. Default is "openai".

    Returns:
        FAISS: The loaded FAISS vector store.
    """
    embeddings = get_embeddings(embedding_type)

    try:
        vectorstore = FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
        logging.info(f"Successfully loaded FAISS index from {path}")
        return vectorstore
    except Exception as e:
        logging.error(f"Failed to load FAISS index from {path}: {e}")
        raise RuntimeError(f"Error loading FAISS index: {e}")