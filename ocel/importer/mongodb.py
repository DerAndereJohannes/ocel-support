import copy
from pymongo import MongoClient


def apply(db):
    log = {}
    others_collection = db["ocel:others"]
    events_collection = db["ocel:events"]
    objects_collection = db["ocel:objects"]
    events = {}
    for ev in events_collection.find():
        ev2 = copy.copy(ev)
        events[ev2["ocel:id"]] = ev2
        del ev2["ocel:id"]
        del ev2["ocel:omapWId"]
        del ev2["_id"]
    objects = {}
    for obj in objects_collection.find():
        obj2 = copy.copy(obj)
        objects[obj["ocel:id"]] = obj2
        del obj2["ocel:id"]
        del obj2["_id"]
    log["ocel:events"] = events
    log["ocel:objects"] = objects
    other = list(others_collection.find())
    del other[0]["_id"]
    del other[1]["_id"]
    del other[2]["_id"]
    log["ocel:global-event"] = other[0]
    log["ocel:global-object"] = other[1]
    log["ocel:global-log"] = other[2]
    return log
