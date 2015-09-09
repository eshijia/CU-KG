# -*- coding: utf-8 -*-

import json
import requests


class CayleyClient(object):
    def __init__(self, host='localhost', port='64210', version='1'):
        self.base_url = 'http://%s:%s/api/v%s' % (host, port, version)
        self.query_url = self.base_url + '/query/gremlin'
        self.write_url = self.base_url + '/write'
        self.delete_url = self.base_url + '/delete'

    def query(self, data):
        response = requests.post(self.query_url, data=str(data))
        return response.status_code, response.json()

    def write(self, data):
        response = requests.post(self.write_url, data=str(data))
        return response.status_code, response.json()

    def delete(self, data):
        response = requests.post(self.delete_url, data=str(data))
        return response.status_code, response.json()


class _CayleyGremlinQuery(object):
    def __init__(self):
        self.queryUnits = []

    def __str__(self):
        return '.'.join([str(q) for q in self.queryUnits])

    def append(self, method, *parameters):
        if len(parameters) > 0:
            self.queryUnits.append(method % parameters)
        else:
            self.queryUnits.append(method)


class CayleyDelete(object):
    def __init__(self):
        self.deleteQuads = []

    def append(self, subject, predicate, object):
        delete_dict = {"subject": "%s" % subject,
                       "predicate": "%s" % predicate,
                       "object": "%s" % object}
        self.deleteQuads.append(delete_dict)

    def __str__(self):
        return json.dumps(self.deleteQuads)


class CayleyWrite(object):
    def __init__(self):
        self.writeQuads = []

    def append(self, subject, predicate, object):
        write_dict = {"subject": "%s" % subject,
                      "predicate": "%s" % predicate,
                      "object": "%s" % object}
        self.writeQuads.append(write_dict)

    def __str__(self):
        return json.dumps(self.writeQuads)


class CayleyPath(_CayleyGremlinQuery):
    def __init__(self, parent):
        super(CayleyPath, self).__init__()
        self.append(parent)

    def __format_value(self, value):
        if value == 'null':
            return value
        elif type(value) is str:
            return "'%s'" % value
        elif type(value) is dict:
            return json.dumps(value)

        return value

    def __extend(self, method, predicate=None, tags=None):
        if predicate is None and tags is None:
            self.append("%s()", method)
        elif tags is None:
            self.append("%s(%s)", method, self.__format_value(predicate))
        else:
            self.append("%s(%s, %s)", method,
                          self.__format_value(predicate),
                          self.__format_value(tags))
        return self

    def Out(self, predicate=None, tags=None):
        self.__extend('Out', predicate, tags)
        return self

    def In(self, predicate=None, tags=None):
        self.__extend('In', predicate, tags)
        return self

    def Both(self, predicate=None, tags=None):
        self.__extend('Both', predicate, tags)
        return self

    def Tag(self, *tags):
        self.append('Tag(%s)', json.dumps(tags))
        return self

    def All(self):
        self.append('All()')
        return self

    def GetLimit(self, limit):
        self.append('GetLimit(%s)', limit)
        return self


class CayleyGraphObject(object):
    def V(self):
        return CayleyPath('g.V()')

    def M(self):
        return CayleyPath('g.Morphism()')

    def Vertex(self):
        return self.V()

    def Morphism(self):
        return self.M()

    def V(self, *nodes):
        return CayleyPath("g.V({0:s})".format(
            ",".join(["'%s'" % node for node in nodes])))

    def Vertex(self, *nodes):
        return self.V(nodes)
