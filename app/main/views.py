#!/use/bin/env python
# -*- coding=utf-8 -*-
from flask import request, jsonify
from data import bmes_participle
from . import main
import finalseg
import jieba
import jieba.posseg
import jieba.analyse

def cut_sentence(sentence):
    seg_list = jieba.cut(sentence=sentence, HMM=True)
    return '/'.join(seg_list)

def cut_ansj(sentence):
    words = jieba.posseg.cut(sentence=sentence, HMM=True)
    ans = []
    for word, flag in words:
        if flag == 'nr':
            ans.append('/'.join([word, flag]))
    return ','.join(ans)

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

methods = {'hmm_participle': participle_text, }

@main.route('/index', methods=['GET'])
def index():
    return 'runing'

@main.route('/api/nlp', methods=['POST'])
def post_nlp():
    verification(request)
    rejs = request.json
    data = rejs.get('data')
    action = rejs.get('action')
    method = data.get('method')
    if method == 'hmm_participle':
        cut_result = participle_text(data.get('text'))
        return jsonify({'result': 'success', 'cut_result': cut_result})
    if method == 'default':
        sentence = data.get('text')
        seg_list = finalseg.cut(sentence)
        res = "/ ".join(seg_list)
        return jsonify({'result': 'success', 'cut_result': res})
    if method =='seg_hmm':
        sentence = data.get('text')
        seg_str = cut_sentence(sentence)
        return jsonify({'result': 'success', 'cut_result': seg_str})
    if method == 'ner_hmm':
        sentence = data.get('text')
        ner_cut = cut_ansj(sentence)
        return jsonify({'result': 'success', 'cut_result': ner_cut})