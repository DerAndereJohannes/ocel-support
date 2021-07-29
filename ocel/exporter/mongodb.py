import copy


def export(log, db):
    print(log.keys())
    others_collection = db["ocel:others"]
    events_collection = db["ocel:events"]
    objects_collection = db["ocel:objects"]
    events = []
    for k in log["ocel:events"]:
        events.append(copy.copy(log["ocel:events"][k]))
        events[-1]["ocel:id"] = k
        omapWId = []
        for o in log["ocel:events"][k]["ocel:omap"]:
            omapWId.append(o + "_" + k)
        events[-1]["ocel:omapWId"] = omapWId
    events_collection.insert_many(events)
    events_collection.create_index([("ocel:id", 1)])
    events_collection.create_index([("ocel:activity", 1)])
    events_collection.create_index([("ocel:omap", 1)])
    objects = []
    for k in log["ocel:objects"]:
        objects.append(copy.copy(log["ocel:objects"][k]))
        objects[-1]["ocel:id"] = k
    objects_collection.insert_many(objects)
    objects_collection.create_index([("ocel:id", 1)])
    objects_collection.create_index([("ocel:type", 1)])
    ocel_global_event = copy.copy(log["ocel:global-event"])
    ocel_global_object = copy.copy(log["ocel:global-object"])
    ocel_global_log = copy.copy(log["ocel:global-log"])
    others_collection.insert_many([ocel_global_event, ocel_global_object, ocel_global_log])

