#!/use/bin/env python
# -*- coding=utf-8 -*-
from flask import Flask, request
from data import bmes_participle
app = Flask(__name__)

@app.route('api/nlp', methods=['POST'])
def post_nlp():
    if not request.json or not


bmes_participle.cut_sentence()

