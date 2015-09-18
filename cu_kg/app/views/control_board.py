# -*- coding: utf-8 -*-

import json

from flask import Blueprint, render_template, request, redirect, url_for

from cu_kg.mp.db.mongodb.datatables import DataTablesServer
from cu_kg.mp.db.mongodb.utils import delete_quads as delete_quads_mongodb
from cu_kg.mp.db.mongodb.utils import update_quads
from cu_kg.mp.db.cayley.utils import write_quad

control_board = Blueprint('control_board', __name__,
                          template_folder='../templates',
                          static_folder='../static')


@control_board.route('/')
def cb_base():
    classify_name = u'分类关系'
    classify_description = u'三元组的Predicate值为"is-a"或"instance-of"，' \
                           u'该类三元组构成了整个知识库的分类体系'

    attribute_name = u'属性关系'
    attribute_description = u'三元组的Predicate值的前缀为"attribute:"，' \
                            u'表示某一实体Subject的属性Predicate的值为Object'

    common_name = u'普通关系'
    common_description = u'普通的三元组，该类三元组数据在知识库中的数据量最大'

    return render_template('control_board/cb_base.html', **locals())


@control_board.route('/cb_classify')
def classify_quads():
    return render_template('control_board/cb_classify.html')


@control_board.route('/classify_quads')
def get_classify_quads():
    return get_quads(request, 0)


@control_board.route('/cb_attribute')
def attribute_quads():
    return render_template('control_board/cb_attribute.html')


@control_board.route('/attribute_quads')
def get_attribute_quads():
    return get_quads(request, 1)


@control_board.route('/cb_common')
def common_quads():
    return render_template('control_board/cb_common.html')


@control_board.route('/common_quads')
def get_common_quads():
    return get_quads(request, 2)


def get_quads(request, type):
    results = DataTablesServer(request, type).result()
    return json.dumps(results)


@control_board.route('/delete_quads')
def delete_quads():
    temp_subject = request.args.get('subject')
    temp_predicate = request.args.get('predicate')
    temp_object = request.args.get('object')

    result = delete_quads_mongodb(temp_subject, temp_predicate, temp_object)
    return json.dumps({"result": result})


@control_board.route('/add_quads', methods=['POST'])
def add_quads():
    temp_subject = request.form.get('subject')
    temp_predicate = request.form.get('predicate')
    temp_object = request.form.get('object')
    temp_time = request.form.get('time')

    # add quads by cayley and then edit attributes by mongodb
    result1 = write_quad(temp_subject, temp_predicate, temp_object)
    result2 = update_quads(temp_subject, temp_predicate, temp_object,
                           timestamp=temp_time)

    return json.dumps({"result": result1 and result2})


@control_board.route('/edit_quads', methods=['POST'])
def edit_quads():
    temp_subject = request.form.get('subject')
    temp_predicate = request.form.get('predicate')
    temp_object = request.form.get('object')
    temp_time = request.form.get('time')

    result = update_quads(temp_subject, temp_predicate, temp_object,
                          timestamp=temp_time)
    return json.dumps({"result": result})

