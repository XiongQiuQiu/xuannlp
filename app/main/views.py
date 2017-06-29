#!/use/bin/env python
# -*- coding=utf-8 -*-
from flask import request, jsonify
from data import bmes_participle
from . import main


def participle_text(text):
    ans = []
    prob_path = bmes_participle.cut_sentence(text)
    for i in zip(text, prob_path):
        ans.append(i[0]+' ' if i[1] == 'E' or i[1] == 'S' else i[0])
    return ''.join(ans)

def verification(request):
    if not request.json:
        return jsonify({'result': 'fail', 'reason': 'parse fail'}), 200
    requ = request.json
    if requ.get('token') != 'Ywjo0ei9XeMOBrAj':
        return jsonify({'result': 'fail', 'reason': 'token is wrong'}), 200
    if not requ.get('action'):
        return jsonify({'result': 'fail', 'reason': 'must have action'}), 200
    if not requ.get('data'):
        return jsonify({'result': 'fail', 'reason': 'must have data'}), 200
    text = requ.get('data').get('text')
    if isinstance(text, unicode):
        return jsonify({'result': 'fail', 'reason': 'text must unicode'}), 200

methods = {'hmm_participle': participle_text}

@main.route('/index', methods=['GET'])
def index():
    return 'runing'

@main.route('/api/nlp', methods=['POST'])
def post_nlp():
    verification(request)
    rejs = request.json
    data = rejs.get('data')
    action = rejs.get('action')
    if data.get('method') in methods:
        method = methods.get(data.get('method'))
        cut_result = method(data.get('text'))
        print data.get('text')
        return jsonify({'result': 'success', 'cut_result': cut_result})
    else:
        return jsonify({'result': 'fail', 'reason': 'not support method'}), 200
