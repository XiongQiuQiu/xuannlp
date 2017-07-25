# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import jieba.posseg
app = Flask(__name__)
def cut_ansj(sentence):
    words = jieba.posseg.cut(sentence=sentence, HMM=True)
    ans = []
    for word, flag in words:
        if flag == 'nr':
            ans.append('/'.join([word, flag]))
    return ','.join(ans)

@app.route('/')
def hello_world():
    sentence = u'姚晨和凌潇肃离婚了'
    ner_cut = cut_ansj(sentence)
    return jsonify({'result': 'success', 'cut_result': ner_cut})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
