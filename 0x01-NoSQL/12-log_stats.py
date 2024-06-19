#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    print(log_collection.count_documents({}))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        method_cound = log_collection.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, method_cound))

    status_count = log_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print('{} status check'.format(status_count))
