# -*- coding: utf-8 -*-

import json

from flask import Blueprint, render_template

from cu_kg.mp.db.mongodb.utils import get_quads_count, get_nodes_count

home = Blueprint('home', __name__,
                 template_folder='../templates',
                 static_folder='../static')


@home.route('/')
def index():
    body_head = u'Content Understanding - Knowledge Graph'

    content_head = u'CU-KG（面向内容理解的知识图谱）'

    content_body = u'是一套可供文本内容语义理解使用的知识图谱，具有千万级的实体和亿级的关系。' \
                   u'对于给定的文本内容能够对其中的显式实体与隐式实体间进行关系发现与建模，' \
                   u'并且给出各关系的可信性排序。'

    return render_template('home/home.html', **locals())


@home.route('/count', methods=['POST'])
def get_count():
    quads_count = get_quads_count()
    nodes_count = get_nodes_count()

    count_dict = {'quads': quads_count, 'nodes': nodes_count}
    return json.dumps(count_dict)
