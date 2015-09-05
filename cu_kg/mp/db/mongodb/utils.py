# -*- coding:utf-8 -*-

from cu_kg.config import MongoDBConfig
from common import init_client, close_client, get_database, get_collection

QUADS_FIELD = (
    SUBJECT, PREDICATE, OBJECT, LABEL, TIMESTAMP, URLS
) = (
    'subject', 'predicate', 'object', 'label', 'timestamp', 'urls'
)


def init_db_cayley():
    client = init_client(MongoDBConfig.MONGODB_HOST,
                         MongoDBConfig.MONGODB_PORT)
    db = get_database(client, MongoDBConfig.DATABASE_NAME)
    return client, db


def get_quads_collection(db):
    return get_collection(db, MongoDBConfig.COLLECTION_QUADS)


def get_nodes_collection(db):
    return get_collection(db, MongoDBConfig.COLLECTION_NODES)


def get_quads(subject, predicate, object):
    client, db = init_db_cayley()
    quads = get_quads_collection(db)
    result = quads.find_one({SUBJECT: subject, PREDICATE: predicate,
                             OBJECT: object})
    close_client(client)
    return result


def update_quads(subject, predicate, object, **kwargs):
    client, db = init_db_cayley()
    quads = get_quads_collection(db)

    attr_dict = {}
    if LABEL in kwargs:
        attr_dict[LABEL] = kwargs[LABEL]
    if URLS in kwargs:
        attr_dict[URLS] = kwargs[URLS]
    if TIMESTAMP in kwargs:
        attr_dict[TIMESTAMP] = kwargs[TIMESTAMP]

    updated = False
    if attr_dict:
        result = quads.update({SUBJECT: subject,
                               PREDICATE: predicate,
                               OBJECT: object},
                              {'$set': attr_dict})
        updated = result['updatedExisting']

    close_client(client)
    return updated


def delete_quads(subject, predicate, object):
    client, db = init_db_cayley()
    quads = get_quads_collection(db)

    result = quads.remove({SUBJECT: subject, PREDICATE: predicate,
                           OBJECT: object})
    return True if result['n'] else False


def get_quads_count():
    client, db = init_db_cayley()
    nodes = get_nodes_collection(db)
    count = nodes.find().count()
    close_client(client)
    return count


def get_nodes_count():
    client, db = init_db_cayley()
    nodes = get_nodes_collection(db)
    count = nodes.find().count()
    close_client(client)
    return count
