# Semantic search on podcast transcripts using Weaviate Docker
This project's origin is [here](https://github.com/weaviate/weaviate-examples/tree/main/podcast-semantic).

In this tutorial we create a vector store that can be queried using semantic search on a sample dataset composed of transcribed podcasts. The steps will include uploading the data file from a local store, and creating a schema as well as an object store.

(TODO: Add demo video)

We will implement semantic search with the text2vec_openai vectorization module and the text-embedding-ada-002 model.

nearText is used to retrieve query results based on the cosine distance between their vectors. Refer to the [nearText documentation](https://weaviate.io/developers/weaviate/api/graphql/search-operators#neartext) to customize your variable setup.
 

## Setup
### Weaviate is not installed: 
Refer to the instructions [here](https://weaviate.io/developers/weaviate/installation). To summarize, start or create a virtual environment, clone the git repository and run the .yml file using docker.

### Weaviate is already installed:
Ensure that you have the Weaviate client using “pip install weaviate_client” in your terminal. 

## Steps 
1. Run your virtual environment 
    - Anaconda: conda activate myenv where myenv can be the name or the path, or
    - Python: source bin/activate
2. Fork and clone this repository using git clone in your terminal.
3. Use docker-compose up -d to run the .yml file
4. Run the requirements.txt file
6. Edit and run the query.py file to view the results for modified queries.

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
The file podcast_ds2.json was used for the tutorial. Given the api rate limits and cost to run the queries, the first four records were cut to less than half their length and used to test. It is advisable to use shorter summaries when using text2vec_openai on your own data.
