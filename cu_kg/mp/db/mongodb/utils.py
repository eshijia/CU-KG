# -*- coding:utf-8 -*-

from pymongo import MongoClient

from cu_kg.config import MongoDBConfig


def init_client():
    client = MongoClient(MongoDBConfig.MONGODB_HOST,
                         MongoDBConfig.MONGODB_PORT)
    return client


def close_client(client):
    client.close()


def get_database(client, name):
    db = client[name]
    return db


def get_collection(db, name):
    collection = db[name]
    return collection


def get_quads(subject, predicate, object):
    pass


def update_quads(subject, predicate, object):
    pass


def delete_quads(subject, predocate, object):
    pass


def get_quads_count():
    pass


def get_nodes_count():
    pass






