# encoding: utf-8
"""
@Version: Pytcharm
@Author: zwl
@File: tmp02.py
@Time: 2023/1/15 20:27
"""

import time, json

dic = [
    {
        "alarm_type": "A故障",
        "time": "2022-12-19 17:16:11",
        "address": "世界之窗",
        "id_number": "A8O0002",
        "异常时间": 158
    },
    {
        "alarm_type": "A故障",
        "time": "2022-12-19 17:16:11",
        "address": "天河区",
        "id_number": "A8O0000",
        "异常时间": 155
    },
    {
        "alarm_type": "B故障",
        "time": "2022-12-19 15:12:52",
        "address": "世界之窗",
        "id_number": "A8O0002",
        "异常时间": 559
    },
    {
        "alarm_type": "B故障",
        "time": "2022-12-19 15:08:48",
        "address": "天河区",
        "id_number": "A8O0000",
        "异常时间": 312
    },
    {
        "alarm_type": "C故障",
        "time": "2022-12-19 15:02:49",
        "address": "世界之窗",
        "id_number": "A8O0002",
        "异常时间": 150
    },
    {
        "alarm_type": "C故障",
        "time": "2022-12-19 14:42:13",
        "address": "天河区",
        "id_number": "A8O0000",
        "异常时间": 50
    }
]

all_time = int((time.time() - time.timezone)) % 86400
result = {}
for source_i in dic:
    if source_i['id_number'] in result:
        abnormal_time = result[source_i['id_number']]['总异常时间'] + source_i['异常时间']
        result[source_i['id_number']]['总异常时间'] = abnormal_time
        result[source_i['id_number']]['{}率'.format(source_i['alarm_type'])] = '{}%'.format(
            round(source_i['异常时间'] / all_time * 100, 2))
        if time.strptime(source_i['time'], '%Y-%m-%d %H:%M:%S') < time.strptime(
                result[source_i['id_number']]['begin_time'], '%Y-%m-%d %H:%M:%S'):
            result[source_i['id_number']]['begin_time'] = source_i['time']
    else:
        result[source_i['id_number']] = {
            '总异常时间': source_i['异常时间'],
            '总时间': all_time,
            'id_number': source_i['id_number'],
            'address': source_i['address'],
            # 'begin_time': time.strftime('%Y-%m-%d %H:%M:%S'),
            'begin_time': source_i['time'],
            '正常时间': '{}h'.format(round((all_time - source_i['异常时间']) / 60 / 60, 2)),
            '{}率'.format(source_i['alarm_type']): '{}%'.format(round(source_i['异常时间'] / all_time * 100, 2)),

        }

for result_i in result:
    all_normal_time = all_time - result[result_i]['总异常时间']
    result[result_i]['正常率'] = '{}%'.format(round(all_normal_time / all_time * 100, 2))

print(json.dumps(result, indent=4, ensure_ascii=False))
