import data_import

"""Semantic Search 
Next you implement the pipeline and query your data, such as semantic search, generative search, question/answering. In this example we use nearText with the module text2vec-openai which implments text-embedding-ada-002. """

response = (
    client.query
    .get("Podcast", ["transcript"])
    .with_near_text({"concepts": ["semantic search"]})
    .with_limit(3)
    .with_additional(["distance"])
    .do()
)

print(json.dumps(response, indent=2))