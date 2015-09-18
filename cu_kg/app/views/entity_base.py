# -*- coding: utf-8 -*-

import json

from flask import Blueprint, render_template, request

from cu_kg.mp.db.cayley.utils import get_direct_relation
from cu_kg.mp.db.mongodb.utils import search_entity_by_name

entity_base = Blueprint('entity_base', __name__,
                        template_folder='../templates',
                        static_folder='../static')


@entity_base.route('/')
def eb_base():
    return render_template('entity_base/eb_base.html')


@entity_base.route('/search', methods=['POST'])
def search_by_name():
    entity_name = request.form.get('name')
    entity_desc_list = search_entity_by_name(entity_name)
    return json.dumps({"result": entity_desc_list})


@entity_base.route('/<entity_name>')
def eb_info(entity_name):
    entities = []
    relations = []
    text_attrs = []
    pic_attrs = []
    video_attrs = []

    status, result = get_direct_relation(entity_name.encode('UTF-8'))
    if status and result is not None:
        for quad in result['result']:
            temp_subject = quad['subject']
            temp_preidicate = quad['predicate']
            temp_object = quad['object']

            if temp_object not in entities and not \
                    temp_preidicate.startswith('attribute:'):
                entities.append(temp_object)

            if temp_preidicate not in relations and not \
                    temp_preidicate.startswith('attribute:'):
                relations.append(temp_preidicate)

            if temp_preidicate.startswith('attribute:'):
                if temp_preidicate.startswith('attribute:pic'):
                    pic_attrs.append(temp_object)
                elif temp_preidicate.startswith('attribute:video'):
                    video_attrs.append(temp_object)
                else:
                    text_attrs.append(temp_object)

    return render_template('entity_base/eb_info.html', entity_name=entity_name,
                           entities=entities, relations=relations,
                           text_attrs=text_attrs, pic_attrs=pic_attrs,
                           video_attrs=video_attrs, data=result)

