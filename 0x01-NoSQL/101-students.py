#!/usr/bin/env python3
"""List all students sorted by average score"""


def top_students(mongo_collection):
    """
    mongo_collection: pymongo collection object

    Returns: list of students sorted by average score
    """
    top_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_students
