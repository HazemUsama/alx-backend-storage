#!/usr/bin/env python3
"""School by topic"""


def schools_by_topic(mongo_collection, topic):
    """
    mongo_collection: pymongo collection object
    topic: string

    Returns: list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
