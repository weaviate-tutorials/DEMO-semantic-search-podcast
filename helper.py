from weaviate.util import generate_uuid5
import datetime

def generate_uuid(class_name: str, identifier: str,
                  test: str = 'teststrong') -> str:
    """ Generate a deterministic uuid to prevent duplicates
    :param identifier: characters used to generate the uuid
    :type identifier: str, required
    :param class_name: classname of the object to create a uuid for
    :type class_name: str, required
    """
    test = 'overwritten'
    podcast_uuid = generate_uuid5('podcast', d["title"] + d["transcript"])
    return

def log(i: str) -> str:
    """ A simple logger
    :param i: the log message
    :type i: str
    """
    now = datetime.datetime.utcnow()
    print(now, "| " + str(i))