# Run virtual environment and docker

import weaviate
from weaviate.util import generate_uuid5
import json
import helper


# Instatiate the client with rest API
client = weaviate.Client("http://localhost:8080")

# Print the client information to confirm the modules are loaded.
meta_info = client.get_meta()
print(json.dumps(meta_info, indent=2))


"""Setup the schema, an outline requiring the data type, vectorizer and the list of classes. Note that it is essential to have your data cleaned and the categories clearly identified for this step. If using your own vectorizer, "none" should be specified for "vectorizer". """


client.schema.delete_class("Podcast")
schema = {
    "classes": [
        {
            "class": "Podcast",
            "vectorizer": "text2vec-transformers",
            "properties": [
                {
                    "name": "title",
                    "dataType": ["text"]
                },
                {
                    "name": "transcript",
                    "dataType": ["text"]
                }
            ]
        }
    ]
}
client.schema.create(schema)


"""In the following we load the locally stored data (in json format) and create a function definition for an add_podcast object. 

The name of the object represents the highest level classification for your data, indicated below as podcast_object (in dictionary type). Target class represents the next level in the classification of your data. Here we indicate it below as the string "Podcast", but note that multiple classes could have been specified, for example, if we had different categories of podcasts, such as English, Spanish, etc.

The function definition below is implementing batch_size=50. Note that with larger amounts of data you will want to adjust this setting. Per the documentation: "batch imports are used to maximize import speed and minimize network latency. Batch import processes multiple objects per request, and clients can parallelize the process."""

# Load and inspect your data
with open("data/podcast_ds.json", 'r') as f:
    datastore = json.load(f)

print(json.dumps(datastore[0], indent=2))


"""In the cell below we define the batch and the uuid.
Batch definition is helpful because it's "a way of importing/creating objects and references in bulk using a single API request to the Weaviate server."""


def add_podcasts(batch_size=50):
    client.batch.configure(batch_size=1)
    with client.batch as batch:
        for i, d in enumerate(datastore):
            print(f"importing podcast: {i+1}")
            properties = {
                "title": d["title"],
                "transcript": d["transcript"]
            }
            podcast_uuid = generate_uuid5(
                'podcast', d["title"] + d["transcript"])

            batch.add_data_object(
                data_object=properties,
                class_name="Podcast",
                uuid=podcast_uuid)
    client.batch.create_objects()


add_podcasts(1)
