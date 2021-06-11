#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import json

script_path = os.path.split(os.path.realpath(sys.argv[0]))[0]
with open(script_path+'\input.json', 'r', encoding='utf-8') as f:
    data = f.read()
lst = []
loaded = json.loads(data)
for x, element in enumerate(loaded):
    question = {
        'index': 0,
        'subject': '马原',
        'type': '',
        'title': '',
        'answer': ''
    }
    question['index'] = x+1
    if element['stlx'] == 'SC':
        question['type'] = '单选'
    elif element['stlx'] == 'MC':
        question['type'] = '多选'
    else:
        question['type'] = '判断'
    ansstr = element['da']
    if 'A' in ansstr:
        question['answer'] = ''.join(
            [question['answer'], element['xx1'][2:].strip()+'\n'])
    if 'B' in ansstr:
        question['answer'] = ''.join(
            [question['answer'], element['xx2'][2:].strip()+'\n'])
    if 'C' in ansstr:
        question['answer'] = ''.join(
            [question['answer'], element['xx3'][2:].strip()+'\n'])
    if 'D' in ansstr:
        question['answer'] = ''.join(
            [question['answer'], element['xx4'][2:].strip()+'\n'])
    if 'E' in ansstr:
        question['answer'] = ''.join(
            [question['answer'], element['xx5'][2:].strip()+'\n'])
    if ansstr == '对' or ansstr == '错':
        question['answer'] = ansstr
    question['answer'] = question['answer'].strip()
    question['title'] = element['wt']
    lst.append(question)
final = json.dumps(lst, ensure_ascii=False)
with open(script_path+'\data.json', 'w', encoding='utf-8') as a:
    a.write(final)
