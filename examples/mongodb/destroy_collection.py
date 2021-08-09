from pymongo import MongoClient

from examples.mongodb.commons import CONNECTION_STRING, DATABASE_NAME
import traceback


def execute_script():
    client = MongoClient(CONNECTION_STRING)
    print("destroying")
    try:
        client.drop_database(DATABASE_NAME)
    except:
        traceback.print_exc()
    print("destroyed")


if __name__ == "__main__":
    execute_script()
