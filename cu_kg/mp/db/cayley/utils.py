# -*- coding: utf-8 -*-

from cu_kg.mp.db.cayley.client import CayleyClient, CayleyGraphObject


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

