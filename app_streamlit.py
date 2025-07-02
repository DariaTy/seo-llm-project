import streamlit as st
from src.data_preprocessing.preprocess import preprocess_article
from src.llm_inference.prompt_engineer import generate_seo_metadata
from src.embedding_search.similarity import find_similar_texts

def main():
    st.title('SEO Metadata Generator')

    # User input
    article = st.text_area("Enter the article text:")
    historical_metadata = st.text_input("Enter historical metadata (comma-separated):")

    if st.button('Generate Metadata'):
        if article and historical_metadata:
            # Preprocess article
            preprocessed_article = preprocess_article(article)

            # Load historical metadata (dummy embeddings for now)
            historical_metadata = historical_metadata.split(',')
            historical_embeddings = [...]  # Replace with actual embeddings
            
            # Generate SEO metadata
            metadata = generate_seo_metadata(preprocessed_article, historical_metadata, historical_embeddings)
            
            # Find similar metadata
            similar_metadata = find_similar_texts(metadata['title'], historical_metadata)
            
            # Display results
            st.subheader("Generated Metadata:")
            st.write(metadata)
            st.subheader("Similar Metadata Found:")
            st.write(similar_metadata)
        else:
            st.error("Please provide both article and historical metadata.")

if __name__ == "__main__":
    main()
