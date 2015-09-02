# -*- coding:utf-8 -*-

import json


class CayleyClient(object):
    def __init__(self, host='localhost', port='64210', version='1'):
        self.base_url = 'http://%s:%s/api/v%s' % (host, port, version)
        self.query_url = self.base_url + '/query/gremlin'
        self.write_url = self.base_url + '/write'
        self.delete_url = self.base_url + '/delete'

    def query(self, data):
        pass

    def write(self, data):
        pass

    def delete(self, data):
        pass


class __CayleyGremlinQuery(object):
    def __init__(self):
        self.queryUnits = []

    def __str__(self):
        return '.'.join([str(q) for q in self.queryUnits])

    def __append(self, method, *parameters):
        if len(parameters) > 0:
            self.queryUnits.append(method % parameters)
        else:
            self.queryUnits.append(method)


class __CayleyPath(__CayleyGremlinQuery):
    def __init__(self):
        pass

    def __format_value(self, value):
        if value is None:
            return 'null'
        elif type(value) is str:
            return "'%s'" % value
        elif type(value) is dict:
            return json.dumps(value)

        return value

    def __extend(self, method, predicate=None, tag=None):
        if predicate is None and tag is None:
            self.__append("%s()", method)
        elif tag is None:
            self.__append("%s(%s)", method, self.__format_value(predicate))
        else:
            self.__append("%s(%s, %s)", method,
                          self.__format_value(predicate),
                          self.__format_value(tag))
        return self

    def Out(self, predicate=None, tag=None):
        self.__extend('Out', predicate, tag)
        return self

    def In(self, predicate=None, tag=None):
        self.__extend('In', predicate, tag)
        return self

    def Both(self, predicate=None, tag=None):
        self.__extend('Both', predicate, tag)
        return self