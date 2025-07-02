from flask import Flask, request, jsonify
from src.data_preprocessing.preprocess import preprocess_article
from src.llm_inference.prompt_engineer import generate_seo_metadata
from src.embedding_search.similarity import find_similar_texts

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the SEO LLM Project!"

@app.route('/generate-metadata', methods=['POST'])
def generate_metadata():
    # Get input article and historical metadata from the request
    article = request.json.get('article')
    historical_metadata = request.json.get('historical_metadata')
    
    if not article or not historical_metadata:
        return jsonify({"error": "Article and historical metadata are required."}), 400
    
    # Preprocess the article
    preprocessed_article = preprocess_article(article)
    
    # Load historical metadata (just an example, you may load embeddings from a database)
    historical_metadata = historical_metadata.split(',')
    historical_embeddings = [...]  # Replace with precomputed embeddings
    
    # Generate SEO metadata
    metadata = generate_seo_metadata(preprocessed_article, historical_metadata, historical_embeddings)
    
    # Find similar metadata using embeddings
    similar_metadata = find_similar_texts(metadata['title'], historical_metadata)
    
    # Return the result as JSON
    return jsonify({
        "generated_metadata": metadata,
        "similar_metadata": similar_metadata
    })

if __name__ == '__main__':
    app.run(debug=True)
