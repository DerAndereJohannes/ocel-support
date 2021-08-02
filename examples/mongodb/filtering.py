from pymongo import MongoClient
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    events_collection = db["ocel:events"]
    aa = time.time_ns()
    activities_filter = events_collection.find({"ocel:activity": {"$in": ["Create Quotation", "Create Order", "Create document (EKKO)"]}})
    for el in activities_filter:
        print(el)
    bb = time.time_ns()
    print("\nTOTAL TIME: ",(bb-aa)/10**9)


if __name__ == "__main__":
    execute_script()
