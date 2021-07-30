from pymongo import MongoClient
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time
from collections import Counter

def execute_script():
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    events_collection = db["ocel:events"]
    objects_collection = db["ocel:objects"]
    ggg = events_collection.aggregate(
        [{"$sort": {"ocel:timestamp": 1}}, {"$unwind": "$ocel:omap"}, {"$group": {'_id': '$ocel:omap', 'Subject': {"$push": '$ocel:activity'}}}, {"$group": {'_id': '$Subject', "count": {"$count": {}}}}])
    for el in ggg:
        print(el)


if __name__ == "__main__":
    execute_script()
