# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
sys.path.append("../")

import jieba
import jieba.posseg
import jieba.analyse

def cut_sentence(sentence):
    seg_list = jieba.cut(sentence=sentence, HMM=True)
    print(", ".join(seg_list))
    seg_list1 = jieba.cut(sentence=sentence, HMM=False)
    print(", ".join(seg_list1))
    words = jieba.posseg.cut(sentence, HMM=True)
    for word, flag in words:
        if flag=='nr':
            print '/'.join([word, flag])
print 'test'
#cut_sentence("姚晨和凌潇肃离婚了")
