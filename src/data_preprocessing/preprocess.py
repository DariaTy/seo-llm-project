import re
from typing import List

def clean_html(text: str) -> str:
    """Remove HTML tags from the text."""
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text

def summarize_text(text: str, max_length: int = 500) -> str:
    """Summarize the article if it’s too long."""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

def preprocess_article(article: str, max_length: int = 500) -> str:
    """Preprocess the article: clean and summarize."""
    cleaned_text = clean_html(article)
    summarized_text = summarize_text(cleaned_text, max_length)
    return summarized_text
