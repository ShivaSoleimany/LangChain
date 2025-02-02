from langchain.embeddings import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer
import os

def get_embedding_model(model_name="openai"):
    """
    Returns an embedding model based on the selected method.

    model_name:
      - "openai" (default) → Uses OpenAI's embeddings
      - "huggingface" → Uses a SentenceTransformer model from Hugging Face
    """

    if model_name.lower() == "openai":
        return OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

    elif model_name.lower() == "huggingface":
        huggingface_token = os.getenv("HUGGINGFACEHUB_API_KEY")

        return SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2",
            use_auth_token=huggingface_token
        ) 
    else:
        raise ValueError("Invalid embedding model. Choose 'openai' or 'huggingface'.")
