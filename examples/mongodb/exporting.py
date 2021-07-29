from pymongo import MongoClient
import ocel
from ocel.exporter import mongodb as mongodb_exporter
from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    try:
        client.drop_database(DATABASE_NAME)
    except:
        pass

    db = client[DATABASE_NAME]
    log = ocel.import_log("../../logs/log.xmlocel")

    mongodb_exporter.apply(log, db)


if __name__ == "__main__":
    execute_script()
