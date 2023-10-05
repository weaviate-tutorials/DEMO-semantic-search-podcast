# Semantic search on podcast transcripts
This project's origin is [here](https://github.com/weaviate/weaviate-examples/tree/main/podcast-semantic).

(TODO: Add Description)

(TODO: Add demo video)

[Vectorization module](https://weaviate.io/developers/weaviate/current/retriever-vectorizer-modules/text2vec-transformers.html#pre-built-images): [`sentence-transformers/msmarco-distilroberta-base-v2`](https://huggingface.co/sentence-transformers/msmarco-distilroberta-base-v2)

## Prerequisites
(TO DO)

## Setup instructions
1. Set-up  Weaviate: `docker-compose up -d`*
2. Install Weaviate client: `pip install weaviate_client==3.2.2`
3. Import data: `python3 import.py`**
4. Query data: Go to [console.semi.technology](https://console.semi.technology/) on Chrome/Safari and connect to http://localhost:9999. Click on Query Module to start querying using GraphQL
 
*Change port `9999` in `docker-compose.yml`  and `import.py` to a different value (like 8888), if not able to connect  
**Could take up to 3 hrs 🙂

## Usage instructions

Example Queries:

Suppose we want to listen to some Changelog episodes discussing GraphQL. We can list the desired episode titles (and transcripts too) via `nearText` for the concept `Episode about graphql`:  


## Dataset license
300 Podcast transcripts from [Changelog](https://github.com/thechangelog/transcripts)  
