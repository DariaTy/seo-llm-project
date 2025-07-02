import openai
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

openai.api_key = "your-openai-api-key"
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_metadata_embedding(metadata: str) -> np.ndarray:
    """Generate an embedding for the given SEO metadata."""
    return model.encode(metadata)

def find_similar_metadata(new_metadata: str, historical_metadata: list, historical_embeddings: np.ndarray) -> dict:
    """Find the most similar metadata from the historical list using cosine similarity."""
    new_embedding = generate_metadata_embedding(new_metadata)
    similarities = cosine_similarity([new_embedding], historical_embeddings)
    most_similar_index = np.argmax(similarities)
    return historical_metadata[most_similar_index], similarities[0][most_similar_index]

def generate_seo_metadata(article_text: str, historical_metadata: list, historical_embeddings: np.ndarray) -> dict:
    """Generate SEO metadata and find similar metadata."""
    prompt = f"""
    Given the article below, generate an SEO-friendly title and description optimized for performance.
    Use the following example metadata from past successful articles to ensure the tone and structure align:
    
    Example Metadata: {historical_metadata}
    
    Article: {article_text}
    
    Title: [SEO-friendly title]
    Meta Description: [SEO-friendly description]
    """
    
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=["\n"]
    )
    
    generated_text = response.choices[0].text.strip()
    title, description = generated_text.split("\n", 1) if "\n" in generated_text else (generated_text, "")
    
    similar_metadata, similarity_score = find_similar_metadata(title, historical_metadata, historical_embeddings)
    
    return {"title": title, "description": description, "similar_metadata": similar_metadata, "similarity_score": similarity_score}
