import os
from langchain import OpenAI
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
import logging
# from langchain.llms import MistralAI

load_dotenv()

def get_llm(temperature: float=0.7, max_tokens: int=500):
    """
    Initializes and returns an OpenAI LLM instance with configurable parameters.

    Args:
        temperature: Controls randomness in LLM responses (0.0 = deterministic, 1.0 = more creative).
        max_tokens: Maximum number of tokens for response generation.

    Returns:
        OpenAI: A configured OpenAI LLM instance.
    """

    return OpenAI(
        model_name="gpt-3.5-turbo-instruct",
        temperature=temperature,
        max_tokens=max_tokens
    )

def get_embeddings(model: str ="openai"):

    """
    Returns the selected embedding model.

    Args:
        model: Embedding model to use. Options:
            - "openai" (default): Uses OpenAI's embeddings.
            - "huggingface": Uses Hugging Face's sentence-transformer embeddings.

    Returns:
        The selected embedding model instance.
    """
    if model == "openai":
        return OpenAIEmbeddings()
    elif model == "huggingface":
        return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    else:
        raise ValueError(f"Invalid embedding model '{model}'. Choose 'openai' or 'huggingface'.")
