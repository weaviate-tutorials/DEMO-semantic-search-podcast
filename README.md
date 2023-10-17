# Semantic search on podcast transcripts using Weaviate Docker
This project's origin is [here](https://github.com/weaviate/weaviate-examples/tree/main/podcast-semantic).

In this tutorial we create a vector store that can be queried using semantic search on a sample dataset composed of transcribed podcasts. The steps will include uploading the data file from a local store, and creating a schema as well as an object store.

(TODO: Add demo video)

We will implement semantic search with text2vec_openai's vectorization module. 

nearText is used to retrieve query results based on the distance between their vectors. Refer to the [nearText documentation](https://weaviate.io/developers/weaviate/api/graphql/search-operators#neartext) to customize your variable setup.

If you have GPU, you may want to consider using the text2vec-transformer module instead. 
[text2vec-transformer](https://weaviate.io/developers/weaviate/current/retriever-vectorizer-modules/text2vec-transformers.html#pre-built-images): 

## Setup
### Weaviate is not installed: 
Refer to the instructions [here](https://weaviate.io/developers/weaviate/installation). To summarize, start or create a virtual environment, clone the git repository and run the .yaml file using docker.

### Weaviate is already installed:
Ensure that you have the Weaviate client using “pip install weaviate_client==3.24.1” in your terminal. 

## Steps
1. Fork and clone this repository using git clone in your terminal. 
2. Update the .yml file with your API keys for OpenAI, Cohere, or Huggingface
3. Run your virtual environment 
    - Anaconda: conda activate myenv where myenv can be the name or the path, or
    - Python: source bin/activate
4. Use docker-compose up -d to run the .yml file
5. Run data_import.py file
6. Edit the query.py file to view the results for modified queries.

## Usage instructions
Update the notebook to include your keys and change the example queries or dataset as desired.

1. Create the schema for your data. Note, this step requires your data to already be formatted and ready for importing by keys or column headers.
2. Load in the data from your local data drive.
3. Define the object, its configurations and batch sizes.
4. Import your object/s as defined.
5. Perform the desired queries on your data.


Example Queries:
1.  .with_near_text({"concepts": ["semantic search"]})
2.  .with_near_text({"concepts": ["generative ai"]})
3.  .with_near_text({"concepts": ["machine learning"]})


## Dataset license
300 Podcast transcripts from [Changelog](https://github.com/thechangelog/transcripts)  
