# -*- coding: utf-8 -*-

from pymongo import MongoClient

from cu_kg.config import MongoDBConfig


class DataTablesServer(object):

    def __init__(self, request, type):
        self.columns = ['subject', 'predicate', 'object']
        self.collection = MongoDBConfig.COLLECTION_QUADS

        self.request_values = request.values

        # 0: classify predicate, 1: attribute predicate, 2: common predicate
        self.type = type

        self.client = MongoClient(host=MongoDBConfig.MONGODB_HOST,
                                  port=MongoDBConfig.MONGODB_PORT)

        self.result_data = None

        self.cardinality = 0
        self.cardinality_filtered = 0

        self.query()

    def pagination(self):
        pages = {}

        if self.request_values['iDisplayStart'] != "" \
            and self.request_values['iDisplayLength'] != -1:
            pages['start'] = int(self.request_values['iDisplayStart'])
            pages['length'] = int(self.request_values['iDisplayLength'])

        return pages

    def filter(self):
        _filter = {}

        if self.request_values.has_key('sSearch') \
            and self.request_values['sSearch'] != "":

            or_filter_on_columns = []
            for i in range(len(self.columns)):
                if self.columns[i] != 'predicate':
                    column_filter = {}
                    column_filter[self.columns[i]] = \
                        {'$regex': self.request_values['sSearch'], '$options': 'i'}
                    or_filter_on_columns.append(column_filter)

            _filter['$or'] = or_filter_on_columns

        if self.type == 0:
            _filter['predicate'] = {'$in': ['is-a', 'instance-of']}
        elif self.type == 1:
            _filter['predicate'] = {'$regex': '^attribute:'}
        elif self.type == 2:
            _filter['predicate'] = {'$regex': '^(?!is-a)(?!instance-of)(?!attribute:)'}

        return _filter

    order_dict = {'asc': 1, 'desc': -1}

    def sort(self):
        _sort = []

        if self.request_values['iSortCol_0'] != "" \
            and int(self.request_values['iSortingCols']) > 0:
            for i in range(int(self.request_values['iSortingCols'])):

                column_number = int(self.request_values['iSortCol_' + str(i)])
                sort_direction = self.request_values['sSortDir_' + str(i)]
                _sort.append((self.columns[column_number],
                              self.order_dict[sort_direction]))

        return _sort

    def query(self):
        _db = self.client.cayley
        _collection = _db[self.collection]

        _pages = self.pagination()
        _filter = self.filter()
        _sort = self.sort()

        predicate_filter = {}
        if self.type == 0:
            predicate_filter = {'predicate': {'$in': ['is-a', 'instance-of']}}

        self.result_data = list(_collection.find(spec=_filter,
                                                 skip=_pages['start'],
                                                 limit=_pages['length'],
                                                 sort=_sort))
        self.cardinality_filtered = _collection.find(spec=_filter).count()
        self.cardinality = _collection.find().count()

    def result(self):
        _result = {}

        _result['sEcho'] = str(self.request_values['sEcho'])
        _result['iTotalRecords'] = str(self.cardinality)
        _result['iTotalDisplayRecords'] = str(self.cardinality_filtered)

        data_rows = []
        for row in self.result_data:
            data_row = {}
            for i in range(len(self.columns)):
                data_row[self.columns[i]] = row[self.columns[i]].replace('"', '\\"')

            if 'timestamp' in row:
                data_row['timestamp'] = row['timestamp']
            else:
                data_row['timestamp'] = ''

            data_row['id'] = self.columns[0] + "=" + data_row[self.columns[0]] + \
                             "&" + self.columns[1] + "=" + data_row[self.columns[1]] + \
                             "&" + self.columns[2] + "=" + data_row[self.columns[2]]
            data_rows.append(data_row)

        _result['aaData'] = data_rows

        return _result



