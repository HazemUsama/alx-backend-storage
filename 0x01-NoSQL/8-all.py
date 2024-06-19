#!/usr/bin/env python3
"""List all documents"""

def list_all(mongo_collection):
    """
    mongo_collection: pymongo collection object
    
    Return: empty list if no document in the collection
    """
    return [doc for doc in mongo_collection.find()]
