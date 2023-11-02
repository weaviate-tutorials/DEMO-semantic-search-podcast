# Semantic search on podcast transcripts
This project's origin is [here](https://github.com/weaviate/weaviate-examples/tree/main/podcast-semantic). In this project, we will be using Weaviate to perform semantic search on podcast transcripts. We will be using the OpenAI text2vec transformer module to vectorize the text. Once the complete data is vectorized and stored, we will be able to perform semantic search on the data.

[Vectorization module](https://weaviate.io/developers/weaviate/current/retriever-vectorizer-modules/text2vec-transformers.html#pre-built-images): [`sentence-transformers/multi-qa-distilbert-cos-v1`](https://huggingface.co/sentence-transformers/multi-qa-distilbert-cos-v1).
Note: if this doesn't work, try [`sentence-transformers/msmarco-distilroberta-base-v2`](https://huggingface.co/sentence-transformers/msmarco-distilroberta-base-v2)

(TODO: Add demo video)

## Prerequisites
Before you can run the project, you need to have Docker, Docker Compose, and Python installed on your machine. Follow the instructions below to install the prerequisites:

### 1. Install Docker:
   - **For Windows and Mac**:
      - Download and install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).
   - **For Linux**:
      - Run the following commands in your terminal:
        ```bash
        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io
        ```

### 2. Install Docker Compose:
   - **For Windows and Mac**:
      - Docker Compose is included with Docker Desktop.
   - **For Linux**:
      - Run the following command in your terminal:
        ```bash
        sudo apt install docker-compose
        ```

### 3. Install Python:
   - Download and install the latest version of Python from [Python's official website](https://www.python.org/downloads/).
   - Verify the installation by running the following command in your terminal:
     ```bash
     python --version
     ```

## Setup instructions
1. **Install virtualenv** (if not already installed):
   ```bash
   pip install virtualenv
   ```
2. **Create a Virtual Environment:** 
   Navigate to the directory where you want to create your virtual environment, then run:
   ```bash
   virtualenv <name_of_virtualenv>
   ```
3. **Activate the Virtual Environment:** 
   On Windows, run:
   ```bash
   .\<name_of_virtualenv>\Scripts\activate
   ```
   On macOS and Linux, run:
   ```bash
   source <name_of_virtualenv>/bin/activate
   ```
4. **Install Python requirements:**
   ```bash
   pip install -r requirements.txt
   ```

5. Export OpenAI API Key:
    ```bash
    export OPENAI_APIKEY=<your_openai_api_key>
    ```

## Usage instructions
1. Start up Weaviate: `docker-compose up -d`. Once completed, Weaviate is running on [`http://localhost:8080`]().
2. Run `python import.py` to import the transcripts into Weaviate.
3. The data is now stored in the Weaviate instance. You can experiment with it using a python notebook or a python file.


## Dataset license
300 Podcast transcripts from [Changelog](https://github.com/thechangelog/transcripts)  
