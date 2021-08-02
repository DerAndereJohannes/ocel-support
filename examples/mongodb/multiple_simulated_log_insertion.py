from pymongo import MongoClient
import ocel
from ocel.exporter import mongodb as mongodb_exporter
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time
from examples.mongodb.log_generation import generate_events_objects


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    try:
        client.drop_database(DATABASE_NAME)
    except:
        pass

    db = client[DATABASE_NAME]
    events_collection = db["ocel:events"]
    objects_collection = db["ocel:objects"]

    num_events = 0

    TARGET = 1000000
    while num_events < TARGET:
        list_events, list_objects = generate_events_objects()
        events_collection.insert_many(list_events)
        objects_collection.insert_many(list_objects)
        num_events += len(list_events)

        print(num_events, "of", TARGET, "(", float(num_events)/float(TARGET) * 100.0, " per cent)")


if __name__ == "__main__":
    execute_script()
