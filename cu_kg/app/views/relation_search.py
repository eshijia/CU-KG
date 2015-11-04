# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

relation_search = Blueprint('relation_search', __name__,
                            template_folder='../templates',
                            static_folder='../static')


@relation_search.route('/')
def rs_base():
    return render_template('relation_search/rs_base.html')
