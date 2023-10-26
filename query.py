import weaviate
import json


client = weaviate.Client("http://localhost:8080")

"""Semantic Search 
Next you implement the pipeline and query your data, such as semantic search, generative search, question/answering. In this example we use nearText with the module text2vec-transformers which implments DilstilROBERTa. """


response = (
    client.query
    .get("Podcast", ["title"])
    .with_near_text({"concepts": ["applications"]})
    .with_limit(3)
    .with_additional(["distance"])
    .do()
)

print(json.dumps(response, indent=2))
