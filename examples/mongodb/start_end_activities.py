from pymongo import MongoClient
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time
from collections import Counter

def execute_script():
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    events_collection = db["ocel:events"]
    objects_collection = db["ocel:objects"]
    aa = time.time_ns()
    ggg = events_collection.aggregate(
        [{"$unwind": "$ocel:omap"}, {"$group": {"_id": "$ocel:omap", "startactivity": {"$first": "$ocel:activity"}}}, {"$group": {"_id": "$startactivity", "count": {"$count": {}}}}], allowDiskUse=True)
    start_activities = Counter({x["_id"]: x["count"] for x in ggg})
    ggg = events_collection.aggregate(
        [{"$unwind": "$ocel:omap"}, {"$group": {"_id": "$ocel:omap", "endactivity": {"$last": "$ocel:activity"}}}, {"$group": {"_id": "$endactivity", "count": {"$count": {}}}}], allowDiskUse=True)
    end_activities = Counter({x["_id"]: x["count"] for x in ggg})
    bb = time.time_ns()
    print(start_activities)
    print(end_activities)
    print("\nTOTAL TIME: ", (bb-aa)/10**9)


if __name__ == "__main__":
    execute_script()
