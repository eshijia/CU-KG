# -*- coding: utf-8 -*-

from cu_kg.mp.db.cayley.client import CayleyClient, CayleyGraphObject
from cu_kg.mp.db.cayley.client import CayleyWrite


def get_direct_relation(name):
    client = CayleyClient()
    g = CayleyGraphObject()
    query_data = g.V(name) \
        .Tag('subject') \
        .Out('null', 'predicate') \
        .Tag('object') \
        .All()
    status_code, result = client.query(query_data)
    if status_code == 200 and result['result'] is not None:
        return True, result
    return False, None


def write_quad(subject, predicate, object):
    client = CayleyClient()
    g = CayleyWrite()
    g.append(subject, predicate, object)
    status_code, result = client.delete(g)
    if status_code == 200:
        return True
    return False

