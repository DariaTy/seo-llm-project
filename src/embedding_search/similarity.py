from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(texts: list) -> np.ndarray:
    """Generate embeddings for a list of texts."""
    return model.encode(texts, convert_to_numpy=True)

def find_similar_texts(query: str, texts: list, top_k: int = 5) -> list:
    """Find the most similar texts to the query using cosine similarity."""
    query_embedding = get_embeddings([query])
    text_embeddings = get_embeddings(texts)
    similarities = cosine_similarity(query_embedding, text_embeddings)
    
    top_indices = similarities[0].argsort()[-top_k:][::-1]
    return [texts[i] for i in top_indices]
