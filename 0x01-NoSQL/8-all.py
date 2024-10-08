#!/usr/bin/env python3

""" Lists all documents in a collection
"""

from pymongo import MongoClient

def list_all(mongo_collection):
    """ Lists documents ina collection or empty
    """
    if mongo_collection is not None:
        return list(mongo_collection.find({}))
    else:
        return []