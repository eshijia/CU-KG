# -*- coding: utf-8 -*-

from pymongo import MongoClient


def init_client(host, port):
    client = MongoClient(host, port)
    return client


def close_client(client):
    client.close()


def get_database(client, name):
    db = client[name]
    return db


def get_collection(db, name):
    collection = db[name]
    return collection
