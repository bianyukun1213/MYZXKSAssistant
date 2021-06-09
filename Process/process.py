#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json

with open('questions.json', 'r', encoding='utf-8') as f:
    data = f.read()
lst = []
loaded = json.loads(data)
for x in loaded:
    question = {
        'index': 0,
        'subject': '马原',
        'type': '',
        'title': '',
        'answer': ''
    }
    question['index'] = loaded.index(x)
    if x['stlx'] == 'SC':
        question['type'] = '单选'
    elif x['stlx'] == 'MC':
        question['type'] = '多选'
    else:
        question['type'] = '判断'
    asstr = x['da']
    if 'A' in asstr:
        question['answer'] += x['xx1'][2:]+'\n'
    if 'B' in asstr:
        question['answer'] += x['xx2'][2:]+'\n'
    if 'C' in asstr:
        question['answer'] += x['xx3'][2:]+'\n'
    if 'D' in asstr:
        question['answer'] += x['xx4'][2:]+'\n'
    if 'E' in asstr:
        question['answer'] += x['xx5'][2:]+'\n'
    if asstr == '对' or asstr == '错':
        question['answer'] = x['da']
    question['answer'] = question['answer'].strip()
    question['title'] = x['wt']
    lst.append(question)
final = json.dumps(lst, ensure_ascii=False)
with open('data.json', 'w', encoding='utf-8') as a:
    a.write(final)
