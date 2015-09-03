# -*- coding:utf-8 -*-

from unittest import TestCase
from cu_kg.mp.db.cayley.client import CayleyClient, CayleyGraphObject


class TestCayleyClient(TestCase):
    def test_query(self):
        client = CayleyClient()
        g = CayleyGraphObject()
        query = g.V() \
            .Tag('subject') \
            .Out('null', 'predicate') \
            .Tag('object') \
            .All()
        status, result = client.query(query)

        print result
        self.assertEqual(status, 200)
        self.assertTrue(len(result) > 0)