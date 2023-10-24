import weaviate
from weaviate import Config
import weaviate.classes as wvc
import json

# Starting up the weaviate client
client = weaviate.Client(
    "http://localhost:8080",
    additional_config=Config(grpc_port_experimental=50051),
    timeout_config = (10000, 10000)
)

# Deleting any prevously existing "WineReviews" collections
print(client.collection.delete("Podcast"))

# Creating a new collection with the defined schema
client.collection.create(
    name="Podcast",
    properties=[
        wvc.Property(
            name="title",
            data_type=wvc.DataType.TEXT,
        ),
        wvc.Property(
            name="transcript",
            data_type=wvc.DataType.TEXT,
        )
    ],
    vectorizer_config=wvc.ConfigFactory.Vectorizer.text2vec_transformers()
)

# Checking is the collection is created successfully or not
print(client.collection.exists("Podcast"))

# Importing the data using pandas
with open("./data/podcast_ds.json", 'r') as f:
    datastore = json.load(f)

# print(datastore[0])

# Getting the collection "WineReviews" that was created earlier
podcast = client.collection.get("Podcast")

# Iterating through the wine_reviews dataset and storing it all in an array to be inserted later
transcripts_to_add = [
    wvc.DataObject(
        properties={
            "title": data["title"] + '.',
            "transcript": data["transcript"],
        },
    )
    for data in datastore
]

# Insertine the data into the collection
response = podcast.data.insert_many(transcripts_to_add[0:3])
print(response.errors) # Used to fetch if there are any errors while inserting the data into the collection

# Fetching any 2 wine reviews from the collection and printing the response
response = podcast.query.fetch_objects(limit=2)
print(response)