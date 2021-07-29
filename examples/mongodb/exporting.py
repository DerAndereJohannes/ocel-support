from pymongo import MongoClient
import ocel
from ocel.exporter import mongodb as mongodb_exporter
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    try:
        client.drop_database(DATABASE_NAME)
    except:
        pass

    db = client[DATABASE_NAME]
    log = ocel.import_log("../../logs/log.xmlocel")

    aa = time.time_ns()
    mongodb_exporter.apply(log, db)
    bb = time.time_ns()
    print("\nTOTAL TIME: ",(bb-aa)/10**9)


if __name__ == "__main__":
    execute_script()
