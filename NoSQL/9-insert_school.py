#!/usr/bin/env python3
"""
insert a new document in a collection named in kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """insert a new document in a collection named in kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
