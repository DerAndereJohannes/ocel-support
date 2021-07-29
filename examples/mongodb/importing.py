from pymongo import MongoClient
import ocel
from ocel.importer import mongodb as mongodb_importer
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE_NAME]
    log = mongodb_importer.apply(db)
    ocel.export_log(log, "prova.jsonocel")


if __name__ == "__main__":
    execute_script()
