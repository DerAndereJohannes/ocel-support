from pymongo import MongoClient
import ocel
from ocel.importer import mongodb as mongodb_importer
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import time


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    log = mongodb_importer.apply(db)

    aa = time.time_ns()
    ocel.export_log(log, "prova.jsonocel")
    bb = time.time_ns()
    print("\nTOTAL TIME: ",(bb-aa)/10**9)


if __name__ == "__main__":
    execute_script()
