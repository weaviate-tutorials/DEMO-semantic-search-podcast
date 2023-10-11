# Semantic search on podcast transcripts
This project's origin is [here](https://github.com/weaviate/weaviate-examples/tree/main/podcast-semantic).

In this tutorial we connect to Weaviate using an embedded instance. A database server is launched from the client instantiation call.

(TODO: Add demo video)

We will implement semantic search with text2vec_openai's vectorization module. 
nearText is used to retrieve query results based on the distance between their vectors. Refer to the [nearText documentation](https://weaviate.io/developers/weaviate/api/graphql/search-operators#neartext) to customize your variable setup.

If you have GPU, you may want to consider using the text2vec-transformer module instead. 
[text2vec-transformer](https://weaviate.io/developers/weaviate/current/retriever-vectorizer-modules/text2vec-transformers.html#pre-built-images): 

## Setup
### Weaviate is not installed: 
Refer to the instructions [here](https://weaviate.io/developers/weaviate/installation). You will need to clone and run it on your computer using docker.

### Weaviate is already installed:
You only need to install the Weaviate client using “pip install weaviate_client==3.24.1” in your terminal. 

## Steps
To summarize the steps and explanations in the notebook:
1. Connect to your instance using your API keys for OpenAI, Cohere, or Huggingface
2. Create the schema for your data. Note, this step requires your data to already be formatted and ready for importing by keys or column headers.
3. Load in the data from your local data drive.
4. Define the object, its configurations and batch sizes.
5. Import your object/s as defined.
6. Specify your nearText setup.
7. Perform the desired queries on your data.

## Usage instructions
Update the notebook to include your keys and change the example queries or dataset as desired.



Example Queries:
1.  .with_near_text({"concepts": ["semantic search"]})
2.  .with_near_text({"concepts": ["generative ai"]})
3.  .with_near_text({"concepts": ["machine learning"]})


## Dataset license
300 Podcast transcripts from [Changelog](https://github.com/thechangelog/transcripts)  
