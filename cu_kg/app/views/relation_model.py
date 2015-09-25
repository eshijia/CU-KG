# -*- coding: utf-8 -*-

import json

from flask import Blueprint, render_template, request

from cu_kg.mp.db.cayley.utils import get_direct_relation

relation_model = Blueprint('relation_model', __name__,
                           template_folder='../templates',
                           static_folder='../static')


@relation_model.route('/', methods=['GET', 'POST'])
def rm_base():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            result = hehe()
            print result
            render_template('relation_model/rm_base.html', result=result)
    return render_template('relation_model/rm_base.html', result=None)


def hehe():
    xian_triples = [('重庆警方', '击毙', '周克华'), ('重庆警方', '刑事拘留', '张贵英'),
                    ('重庆市沙坪坝区人民法院', '开庭审理', '张贵英'),
                    ('四川舟楫律师事务所的律师', '辩护', '张贵英')]
    entities = set()
    relations = []

    for triple in xian_triples:
        entities.add(triple[0])
        entities.add(triple[2])
        relations.append({
           'subject': triple[0],
           'predicate': triple[1],
           'object': triple[2],
           'flag': 0
        })

    for e in entities:
        status, ying_triples = get_direct_relation(e)
        if status:
            for triple in ying_triples:
                relations.append({
                    'subject': triple['subject'],
                    'predicate': triple['predicate'],
                    'object': triple['object'],
                    'flag': 1
                })

    return json.dumps({'result': relations})



