# -*- coding:utf-8 -*-
"""
@author: xcld
@file: combat.py
@time: 2023-01-16 21:51
"""
import json
import time

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

all_time = int(time.time() - time.timezone) % 86400
result = {}
Time_sort = []
Failures_time_sum = 0
Failures_time_sum1 = 0


# rate1, rate2, rate3 = 0.0, 0.0, 0.0


def rate(time_type):  # 计算百分比
    rate_type = time_type / all_time * 100
    return rate_type


def time_sort(time_in):  # 对故障时间排序，提取出最开始故障出现时间
    strptimetodate = time.strptime(time_in, "%Y-%m-%d %H:%M:%S")  # 返回元祖
    strptime = time.mktime(strptimetodate)  # mktime时间数组转成时间戳
    Time_sort.append(strptime)
    Time_sort.sort()
    time_local = time.localtime(Time_sort[0])  # 获得时间元组形式数据
    time_strpt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)  # 格式化
    return time_strpt


def str_type(num, unit):  # 输出格式定义
    cut = round(num, 2)
    comb = str(cut) + unit
    return comb


def new_dict(failures_time_sum, all_time1, id_num, address, beg_time, fail_ratea, fail_rateb, fail_ratec,
             mean_time1, meanrate):  # 新样式字典生成
    result[id_num] = {}
    result[id_num]["总异常时间"] = failures_time_sum
    result[id_num]["总时间"] = all_time1
    result[id_num]["address"] = address
    result[id_num]["begin_time"] = beg_time
    result[id_num]["A故障率"] = fail_ratea
    result[id_num]["B故障率"] = fail_rateb
    result[id_num]["C故障率"] = fail_ratec
    mt2 = str_type(mean_time1 / 60 / 60, "h")
    result[id_num]["正常时间"] = mt2
    mt3 = str_type(meanrate, "%")
    result[id_num]["正常率"] = mt3
    return result


# def failures(alty):  # 判断ABC故障并得出百分率
#     item = alty
#     if item.get("alarm_type") == "A故障":
#         # time_type = item.get("异常时间")
#         rate1 = rate(item.get("异常时间"))
#     elif item.get("alarm_type") == "B故障":
#         # time_type = item.get("异常时间")
#         rate2 = rate(item.get("异常时间"))
#     else:
#         # time_type = item.get("异常时间")
#         rate3 = rate(item.get("异常时间"))
#     return rate1, rate2, rate3


for item in dic:  # 根据 id_number遍历源数据，并提取相应内容
    if item.get("id_number") == "A8O0000":
        id_number = "A8O0000"
        # failures(item)
        Failures_time_sum += item.get("异常时间")
        tiso = time_sort(time_in=item.get("time"))
        mean_time = all_time - Failures_time_sum
        mt = rate(mean_time)

        # new_dict(failures_time_sum=Failures_time_sum, all_time1=all_time, id_num=id_number, address=item.get("address"),
        #          beg_time=tiso,
        #          fail_ratea=rate1, fail_rateb=rate2, fail_ratec=rate3, mean_time1=mean_time, meanrate=mt)
        new_dict(failures_time_sum=Failures_time_sum, all_time1=all_time, id_num=id_number,
                 address=item.get("address"), beg_time=tiso, fail_ratea=3, fail_rateb=4, fail_ratec=5,
                 mean_time1=mean_time, meanrate=mt)
    else:
        id_number = item.get("id_number")
        # failures(item)
        Failures_time_sum1 += item.get("异常时间")
        tiso = time_sort(time_in=item.get("time"))
        mean_time = all_time - Failures_time_sum1
        mt = rate(mean_time)
        new_dict(failures_time_sum=Failures_time_sum1, all_time1=all_time, id_num=id_number,
                 address=item.get("address"), beg_time=tiso, fail_ratea=3, fail_rateb=4, fail_ratec=5,
                 mean_time1=mean_time, meanrate=mt)
print("result=", json.dumps(result, indent=4, ensure_ascii=False))
