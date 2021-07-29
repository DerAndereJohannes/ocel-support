from pymongo import MongoClient
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    objects_collection = db["ocel:objects"]
    aa = time.time_ns()
    object_types = objects_collection.distinct("ocel:type")
    for ot in object_types:
        n_obj = objects_collection.find({"ocel:type": ot}).count()
        print("ot="+ot+" n_obj="+str(n_obj))
    bb = time.time_ns()
    print("\nTOTAL TIME: ",(bb-aa)/10**9)


if __name__ == "__main__":
    execute_script()
