#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import json
from fuzzywuzzy import process
import flask
from flask import request
from loguru import logger

app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def pong():
    return 'Pong!', 200, [('Content-Type', 'text/plain; charset=utf-8')]

@app.route('/search', methods=['GET'])
def search():
    if 'title' in request.args:
        arg_title = request.args['title'].strip()
        if arg_title == '':
            return '缺失 title！', 404, [('Content-Type', 'text/plain; charset=utf-8')]
        logger.info('收到格式正确的请求！')
        logger.info('参数中的题目：%s' % arg_title)
        global titles
        global answers
        result = process.extractOne(arg_title, titles)
        match_title = result[0]
        match_ratio = result[1]
        logger.info('匹配到的题目：%s' % match_title)
        logger.info('匹配率：%d%%' % match_ratio)
        for i, element_answer in enumerate(answers):
            for j, element_title in enumerate(titles):
                if element_title == match_title:
                    break
            if i == j:
                answer = element_answer
                break
        logger.info('答案：%s' % answer.replace('\n','；'))
        return ''.join([match_title, '\n---\n', answer]), 200, [('Content-Type', 'text/plain; charset=utf-8')]
    return '缺失 title！', 404, [('Content-Type', 'text/plain; charset=utf-8')]

if(__name__ == '__main__'):
    data_path = '/ma_data/data.json'
    log_path = '/ma_log'
    arg1 = ''
    if(len(sys.argv)>1):
        arg1 = sys.argv[1]
    if(arg1 != '--container'):
        data_path = os.path.split(os.path.realpath(sys.argv[0]))[0] + data_path
        log_path = os.path.split(os.path.realpath(sys.argv[0]))[0] + log_path
    logger.add(log_path + '/{time}.log', rotation = '00:00', retention = 14)
    logger.info('欢迎使用 Hollis(his2nd.life) 的马院考试助手！')
    logger.info('请访问 https://github.com/bianyukun1213/MYZXKSAssistant 阅读使用文档。')
    logger.info('arg1: %s, data_path: %s, log_path: %s' % (arg1, data_path, log_path))
    if(os.path.isfile(data_path) != True):
        logger.info('数据文件不存在！')
        sys.exit()
    with open(data_path, 'r', encoding = 'utf-8') as f:
        data = f.read()
    loaded = json.loads(data)
    titles = []
    answers = []
    for question in loaded:
        titles.append(question['title'])
        answers.append(question['answer'])
    logger.info('%s 条数据已加载，即将运行服务。' % len(loaded))
    app.run(host = '0.0.0.0', port = 8972)
