import unittest
from src.llm_inference.prompt_engineer import generate_seo_metadata

class TestPromptEngineer(unittest.TestCase):
    def test_generate_metadata(self):
        article = "This is a sample article about machine learning applications."
        historical_metadata = ["SEO Best Practices", "SEO Trends", "Meta Description Techniques"]
        historical_embeddings = [...]  # Precomputed embeddings here
        
        result = generate_seo_metadata(article, historical_metadata, historical_embeddings)
        
        self.assertIn("title", result)
        self.assertIn("description", result)
        self.assertIn("similar_metadata", result)
        self.assertIn("similarity_score", result)

if __name__ == '__main__':
    unittest.main()
