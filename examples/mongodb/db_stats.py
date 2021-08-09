from pymongo import MongoClient

from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import traceback


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    stats = client[DATABASE_NAME].command("dbstats")
    print(stats)


if __name__ == "__main__":
    execute_script()
