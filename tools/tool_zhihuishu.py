#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import time
import json
import requests

LIST_URL = 'https://hike-examstu.zhihuishu.com/zhsathome/randomExercise/queryAnswerSheet?courseId=<COURSE_ID>&isFirst=true&randomExerciseStyle=0&uuid=<UUID>'
DETAIL_URL = 'https://hike-examstu.zhihuishu.com/zhsathome/randomExercise/queryRandomExerciseDetail?courseId=<COURSE_ID>&questionId=<QUESTION_ID>&times=<TIMES>&randomExerciseStyle=0&uuid=<UUID>'

args = sys.argv
course_id = ''
uuid = ''
if len(args) == 3:
    course_id = args[1]
    uuid = args[2]
    list_url = LIST_URL.replace(
        '<COURSE_ID>', course_id).replace('<UUID>', uuid)
    exercises = requests.get(list_url).json()['rt']
    exercise_count = exercises['randomExerciseCount']
    exercise_list = exercises['lists']
    exercise_times = exercises['times']
    print('获取到 %d 道习题。' % exercise_count)
    details = []
    for index, exercise in enumerate(exercise_list):
        print('正在采集习题 %d……(%d/%d)' %
              (exercise['exerciseId'], index + 1, exercise_count))
        detail_url = DETAIL_URL.replace('<COURSE_ID>', course_id).replace(
            '<UUID>', uuid).replace('<QUESTION_ID>', str(exercise['exerciseId'])).replace('<TIMES>', str(exercise_times))
        detail = requests.get(detail_url).json()['rt']
        if detail == None:
            print('跳过习题 %d 的录入：接口返回结果为空，习题可能已被删除。' % exercise['exerciseId'])
        else:
            details.append(detail)
        time.sleep(1)
    print('采集完成，正在保存……')
    save_path = os.path.split(os.path.realpath(sys.argv[0]))[
        0] + '\\from_zhihuishu\\'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    json_file_path = save_path + 'output_' + course_id + '.json'
    json_file = open(json_file_path, mode='w', encoding='utf-8')
    json.dump(details, json_file, ensure_ascii=False, indent=4)
    json_file.close()
    print('完成！')

else:
    print('参数错误！')
