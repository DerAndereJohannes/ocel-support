from pymongo import MongoClient
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time
from collections import Counter

def execute_script():
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    events_collection = db["ocel:events"]
    objects_collection = db["ocel:objects"]
    print(events_collection.count())
    mdfg = {}
    aa = time.time_ns()
    object_types = objects_collection.distinct("ocel:type")
    ggg = events_collection.aggregate(
        [{"$sort": {"ocel:timestamp": 1}}, {"$unwind": "$ocel:omap"}, {"$group": {'_id': '$ocel:omap', 'Subject': {"$push": '$ocel:activity'}}}])
    ggg = {str(x["_id"]): x["Subject"] for x in ggg}
    for ot in object_types:
        objects = objects_collection.find({"ocel:type": ot}).distinct("ocel:id")
        dfg = Counter()
        for ob in objects:
            if ob in ggg:
                lif = ggg[ob]
                for i in range(len(lif)-1):
                    dfg[(lif[i], lif[i+1])] += 1
        mdfg[ot] = dict(dfg)
    bb = time.time_ns()
    print("\nTOTAL TIME: ",(bb-aa)/10**9)
    print(mdfg)


if __name__ == "__main__":
    execute_script()
