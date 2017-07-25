import jieba
import jieba.posseg

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