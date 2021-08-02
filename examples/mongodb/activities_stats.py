from pymongo import MongoClient
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    events_collection = db["ocel:events"]
    aa = time.time_ns()
    activities = events_collection.distinct("ocel:activity")
    for act in activities:
        n_events = events_collection.find({"ocel:activity": act}).count()
        n_unq_obj = len(list(events_collection.aggregate([{"$match": {"ocel:activity": act}}, {"$unwind": "$ocel:omap"}, {"$group": {"_id": "$ocel:omap"}}], allowDiskUse=True)))
        n_tot_obj = len(list(events_collection.aggregate([{"$match": {"ocel:activity": act}}, {"$unwind": "$ocel:omapWId"}, {"$group": {"_id": "$ocel:omapWId"}}], allowDiskUse=True)))
        print("activity="+act+" events="+str(n_events)+" unique objs="+str(n_unq_obj)+" total objs="+str(n_tot_obj))
    bb = time.time_ns()
    print("\nTOTAL TIME: ",(bb-aa)/10**9)


if __name__ == "__main__":
    execute_script()
