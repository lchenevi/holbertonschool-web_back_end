#!/usr/bin/env python3
"""
return mongo_collection
"""


def list_all(mongo_collection):
    """return mongo_collection"""
    return mongo_collection.find()
