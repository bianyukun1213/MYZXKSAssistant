#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import flask
from flask import request, jsonify

app = flask.Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    if 'title' in request.args:
        print('收到格式正确的请求！')
        title = request.args['title']
        print('标题：', title)
        global titles
        global answers
        match = process.extractOne(title, titles)[0]
        print('匹配结果：', match)
        answer = answers[titles.index(match)]
        print('正确答案：', answer.replace('\n', '\\n'))
        return answer, 200, [('Content-Type', 'text/plain; charset=utf-8')]
    return '未提供题干！', 404, [('Content-Type', 'text/plain; charset=utf-8')]


if(__name__ == '__main__'):
    print('欢迎使用 Hollis(his2nd.life) 的马院考试助手！')
    with open('data.json', 'r', encoding='utf-8') as f:
        data = f.read()
    loaded = json.loads(data)
    titles = []
    answers = []
    for question in loaded:
        titles.append(question['title'])
        answers.append(question['answer'])
    print(len(loaded), ' 条数据已加载，即将运行服务。')
    app.run()
