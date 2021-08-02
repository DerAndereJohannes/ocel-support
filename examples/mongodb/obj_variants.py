from pymongo import MongoClient
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time
from collections import Counter

def execute_script():
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    events_collection = db["ocel:events"]
    aa = time.time_ns()
    ggg = events_collection.aggregate(
        [{"$unwind": "$ocel:omap"}, {"$group": {'_id': '$ocel:omap', 'Subject': {"$push": '$ocel:activity'}}}, {"$group": {'_id': '$Subject', "count": {"$count": {}}}}], allowDiskUse=True)
    ggg = Counter({tuple(x["_id"]): x["count"] for x in ggg})
    bb = time.time_ns()
    print(ggg)
    print("\nTOTAL TIME: ",(bb-aa)/10**9)


if __name__ == "__main__":
    execute_script()
