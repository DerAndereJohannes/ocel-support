from pymongo import MongoClient
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time
from statistics import median


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    events_collection = db["ocel:events"]
    aa = time.time_ns()
    #activities_filter = events_collection.find({"ocel:activity": {"$in": ["Create Quotation", "Create Order"]}}, {"ocel:activity": 1, "ocel:timestamp": 1})
    ggg = events_collection.aggregate([{"$match": {"ocel:activity": {"$in": ["Create Quotation", "Create Order"]}}}, {"$sort": {"ocel:timestamp": 1}}, {"$unwind": "$ocel:omap"}, {"$group": {'_id': '$ocel:omap', 'activityComb': {"$push": '$ocel:activity'}, 'timestampComb': {"$push": '$ocel:timestamp'}}}])
    times = []
    for el in ggg:
        activities = el["activityComb"]
        timestamp = el["timestampComb"]
        for i in range(len(activities)-1):
            if activities[i] == "Create Quotation" and activities[i+1] == "Create Order":
                times.append(timestamp[i+1].timestamp() - timestamp[i].timestamp())
    print(median(times))
    bb = time.time_ns()
    print("\nTOTAL TIME: ",(bb-aa)/10**9)


if __name__ == "__main__":
    execute_script()
