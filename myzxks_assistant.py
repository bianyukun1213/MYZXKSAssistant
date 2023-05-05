#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import json
from fuzzywuzzy import process
import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    if 'title' in request.args:
        arg_title = request.args['title'].strip()
        if arg_title == '':
            return '缺失参数“title”！', 404, [('Content-Type', 'text/plain; charset=utf-8')]
        print('收到格式正确的请求！', file=sys.stdout)
        print('---\n参数中的题目：\n%s' % arg_title, file=sys.stdout)
        global titles
        global answers
        result = process.extractOne(arg_title, titles)
        match_title = result[0]
        match_ratio = result[1]
        print('匹配到的题目：\n%s' % match_title, file=sys.stdout)
        print('匹配率：\n%d%%' % match_ratio, file=sys.stdout)
        for i, element_answer in enumerate(answers):
            for j, element_title in enumerate(titles):
                if element_title == match_title:
                    break
            if i == j:
                answer = element_answer
                break
        print('答案：\n%s\n---' % answer, file=sys.stdout)
        return ''.join([match_title, '\n---\n', answer]), 200, [('Content-Type', 'text/plain; charset=utf-8')]
    return '缺失参数“title”！', 404, [('Content-Type', 'text/plain; charset=utf-8')]

if(__name__ == '__main__'):
    print('欢迎使用 Hollis(his2nd.life) 的马院考试助手！', file=sys.stdout)
    print('请访问 https://github.com/bianyukun1213/MYZXKSAssistant 阅读使用文档。', file=sys.stdout)
    data_path = '/ma_data/data.json'
    arg1 = ''
    if(len(sys.argv)>1):
        arg1 = sys.argv[1]
    if(arg1 != '--container'):
        data_path = os.path.split(os.path.realpath(sys.argv[0]))[0] + data_path
    print('从 %s 读取数据文件。' % data_path, file=sys.stdout)
    if(os.path.isfile(data_path) != True):
        print('数据文件不存在！', file=sys.stdout)
        exit
    with open(data_path, 'r', encoding='utf-8') as f:
        data = f.read()
    loaded = json.loads(data)
    titles = []
    answers = []
    for question in loaded:
        titles.append(question['title'])
        answers.append(question['answer'])
    print('%s 条数据已加载，即将运行服务。' % len(loaded), file=sys.stdout)
    app.run(host='0.0.0.0', port=8972)
