import argparse
from src.data_preprocessing.preprocess import preprocess_article
from src.llm_inference.prompt_engineer import generate_seo_metadata
from src.embedding_search.similarity import find_similar_texts

def main():
    parser = argparse.ArgumentParser(description="Generate SEO metadata for articles.")
    parser.add_argument('--article', type=str, required=True, help="Article text to generate metadata.")
    parser.add_argument('--historical_metadata', type=str, required=True, help="Comma-separated historical metadata.")
    
    args = parser.parse_args()
    
    preprocessed_article = preprocess_article(args.article)
    historical_metadata = args.historical_metadata.split(',')
    historical_embeddings = [...]  # Example embeddings
    
    metadata = generate_seo_metadata(preprocessed_article, historical_metadata, historical_embeddings)
    print(f"Generated Metadata: {metadata}")
    
    similar_metadata = find_similar_texts(metadata['title'], historical_metadata)
    print(f"Similar Metadata Found: {similar_metadata}")

if __name__ == "__main__":
    main()
