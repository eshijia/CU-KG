# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

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


@control_board.route('/classify_quads')
def classify_quads():
    pass


@control_board.route('/attribute_quads')
def attribute_quads():
    pass


@control_board.route('/common_quads')
def common_quads():
    pass

