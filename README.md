# SEO LLM Project

## Author: Daria Tychyno

## Project Overview
The SEO LLM Project aims to develop a lightweight, scalable system that generates SEO-friendly metadata for articles (e.g., titles, meta descriptions) using large language models (LLMs). This tool will automate metadata creation for editorial and marketing teams, while ensuring contextual and tonal accuracy in line with SEO best practices.

## Goals
- Automate the generation of SEO-friendly metadata (titles, descriptions).
- Ensure that metadata is contextually accurate and aligned with article tone.
- Create workflows that are transparent, scalable, and editor-friendly.

## Technical Elements
- **Prompt Engineering**: Iterative testing of OpenAI GPT-based prompts to generate correct titles and descriptions.
- **Embedding Search**: Exploration of vector similarity techniques (e.g., OpenAI Embeddings, sentence-transformers) for content clustering.
- **Pipeline Design**: Drafting an end-to-end pipeline to process articles and generate SEO metadata.

## Tools & Stack
- **LLMs**: OpenAI GPT-4 (or GPT-3.5), HuggingFace APIs
- **Embeddings**: OpenAI or sentence-transformers for similarity clustering
- **Codebase**: Python, Jupyter Notebooks for exploration
- **Delivery**: Metadata output in CSV/JSON format or pushed to CMS/staging DB
