from pymongo import MongoClient
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time
from collections import Counter


def execute_script():
    DEBUG = False
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    events_collection = db["ocel:events"]
    objects_collection = db["ocel:objects"]
    if DEBUG:
        print(events_collection.count())
    mdfg = {}
    aa = time.time_ns()
    object_types = objects_collection.distinct("ocel:type")
    ggg0 = events_collection.aggregate(
        [{"$unwind": "$ocel:omap"}, {"$group": {'_id': '$ocel:omap', 'Subject': {"$push": '$ocel:activity'}}}], allowDiskUse=True)
    dictio_activities = {}
    ggg = {}
    for x in ggg0:
        act = tuple(x["Subject"])
        if act not in dictio_activities:
            dictio_activities[act] = act
        else:
            act = dictio_activities[act]
        ggg[x["_id"]] = act
    del ggg0
    if DEBUG:
        print("calculated gggg")
    for ot in object_types:
        if DEBUG:
            print(ot+" 1")
        objects0 = objects_collection.aggregate([{"$match": {"ocel:type": ot}}, {"$group": {"_id": "$ocel:id"}}], allowDiskUse=True)
        if DEBUG:
            print(ot+" 2")
        objects = []
        for x in objects0:
            objects.append(x["_id"])
        del objects0
        if DEBUG:
            print(ot+" 3")
        dfg = Counter()
        for ob in objects:
            if ob in ggg:
                lif = ggg[ob]
                for i in range(len(lif)-1):
                    dfg[(lif[i], lif[i+1])] += 1
        if DEBUG:
            print(ot+" 4")
        mdfg[ot] = dict(dfg)
        if DEBUG:
            print(ot+" 5")
    bb = time.time_ns()
    print("\nTOTAL TIME: ",(bb-aa)/10**9)
    print(mdfg)


if __name__ == "__main__":
    execute_script()
