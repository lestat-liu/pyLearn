
# 一、列表
'''
1.1 列表的介绍
    列表是python的基础数据类型之⼀
    它是以[ ]括起来, 每个元素⽤' , '隔开⽽且可以存放各种数据类型:
    列表相比于字符串. 不仅可以存放不同的数据类型. ⽽且可以存放⼤量的数据.
    32位python可以存放: 536870912个元素, 64位可以存放: 1152921504606846975个元素.

    ⽽且列表是有序的(按照你保存的顺序),有索引, 可以切⽚⽅便取值.
'''

# 1.2 列表的索引和切片
# lst = [1, 1.20, "si字符串", [1,2,5], 11, 55, 10 ]
# print(lst[2])
# print(lst[3])
#
# print(lst[2:6])
# print(lst[2:6:2])


# 1.3 列表的增删改查
# 1.3.1 增--append；insert； extend
# lst = [1, 1.20, "si字符串", [1,2,5], 11, 55, 10 ]
# lst.append("最后追加的内容")
# print(lst)
# lst.insert(0, "前面插入的内容")
# print(lst)
#
# lst2 = [1,2,3]
# lst.extend(lst2)
# print(lst)


# 1.3.2  删--pop；remove；clear；del
# 根据索引删除列表元素
# lst = [1, 1.20, "si字符串", [1,2,5], 11,11, 55, 10 ]
# lst.pop(0)  # 删除最后一个元素
# lst.pop()  # 删除最后一个元素
# lst.pop(2)  # 删除指定索引的元素

# 根据内容删除列表元素，
# lst.remove("si字符串")
# lst.remove(11)  # 只删除找到的第一个元素
# lst.remove(100)  # ValueError: list.remove(x): x not in list
# if "fa" in lst:
#     删除


# lst.clear()  # 清空列表元素

# del lst[1:3]
# print(lst)

# 1.3.3 改--lst[2]=str
# lst = [1, 1.20, "si字符串", [1,2,5], 11,11, 55, 10 ]
# lst[0] = "直接修改"
# print(lst)

# lst[1:3] = [222,333]
# print(lst)

# st = "字符串的修改"
# st[0] = "xiu"

# 1.3.4 查--for循环
# lst = [1, 1.20, "si字符串", [1,2,5], 11,11, 55, 10 ]
# for v in lst:
#     print(v, end="  ")
# print()
#
# for index, v in enumerate(lst):
#     print("  索引是： ",  index , "  内容是： ", v )

# 1.3.5  其他操作
# lst = [1, 1.20, "si字符串", [1,2,5], 11,11, 55, 10 ]
# num = lst.count(11)
# print(num)


# lst2 = [4,5,7,1,9,4,13,3]
# lst2.sort()  # python默认用快排进行排序
# lst2.sort(reverse=True)  # 改为降序

# lst = ["c", "d", "a"]  # 不能对字符、字符串排序
# print(lst.sort())


# lst2 = [1, 11, 3, 2, 1]
# lst3 = [1, 15, 3, 2, 1]
# lst3.reverse()  # 仅对原对象进行翻转，不可赋值
# print(id(lst2))
# print(id(lst3))
# print(lst3)

# flag = 1
# for i in range(len(lst2)):
#     if lst2[i] == lst3[i]:
#         pass
#         # ...
#     else:
#         print("不是回文")
#         flag = 0
#         break
# if flag:
#     print("是回文")
#
#
# print(lst2)


# 1.3.6  列表的嵌套
# lst = [1,[1,2,3], "st", {1:"sfa"}, (1,2)]


# 三、元组
'''
元组: 
    简单理解就是不可变的列表.也可以称为只读列表, 元组也是python的基本数据类型之⼀, ⽤⼩括号括起来,
    可以放任何类型的数据, 查询可以. 循环也可以. 切片也可以. 但就是不能改.
'''
# list与tuple可以随意转换
# t = (1, 2, 5, 6, [1, 2, 3])
# lst = list(t)
# print(lst)
# print(type(lst))


# 索引和切片
# print(t[0])
# print(t[4])
# print(t[:])
# print(t[::-1])

# 循环输出每一个元素
# for v in t:
#     print(v, end="  ")

# tu = (1)
# # tu2 = (1,)
# # print(type(tu))
# # print(type(tu2))

# count、index、len

'''
    t = (1,2, 5, 6,[1,2,3])
    t[4][0]= "fafdas"
    print(t)
    关于不可变, 注意: 
    这⾥元组的不可变的意思是⼦元素不可变. ⽽⼦元素内部的⼦元素是可以变, 
    这取决于⼦元素是否是可变对象. 
'''

# 四、range介绍
# for i in range(10):
#     print(i, end=" ")
# print()
#
# for i in range(1, 10, 2):
#     print(i, end=" ")
# print()
# for i in range(10, 1, -2):
#     print(i, end=" ")

# enumerate

# 五、字典
'''
    字典(dict)是python中唯⼀的⼀个映射类型.他是以{ }括起来的 键值对 组成. 
    在dict中key是唯⼀的. 在保存的时候, 根据key来计算出⼀个内存地址. 然后将key-value保存在这个地址中.
    
    这种算法被称为hash算法, 所以, 切记, 在dict中存储的key-value中的'key'必须是可hash的,
    如果你搞不懂什么是可哈希, 暂时可以这样记, 可以改变的都是不可哈希的,
    那么可哈希就意味着不可变. 这个是为了能准确的计算内存地址⽽规定的.
    
    已知的可哈希(不可变)的数据类型: int, str, tuple, bool
    不可哈希(可变)的数据类型: list, dict, set
    
    字典定义的语法 :
     {key1: value1, key2: value2....}
    注意: key必须是不可变(可哈希)的. value没有要求.可以保存任意类型的数据
'''
# 5.1 key的合法性演示
# dic = {10:"123", "s":123, (1,):343, True:124323}  #  key相同，后面的会覆盖前面的value
# print(dic)
# print(dic[True])

# 不合法的key
# dic3 = {[1,2]:"565"}
# dic5 = {{1:2}:"565"}
# dic3 = {{1,2,3}:"565"}

# 5.2 字典的增删改查及其他操作
# 5.2.1 增
# dic = {}
# dic["name"] = "小明"
# print(dic)
#
# dic.setdefault("age")
# dic.setdefault("name", 12)  # 字典里面有该key，就用原来的
# print(dic)

# 5.2.2 删
# dic = {"k1":121,"k2":"fdsaf", "k3":"小白"}
# ret = dic.pop("k2")
# print(dic)
# print(ret)

# dic.popitem()

# dic.clear()
# print(dic)

# del dic["k1"]
# print(dic)

# 5.2.3 改
# dic = {}
# dic["name"] = "小明"
# print(dic)
# dic["name"] = "小红"
# print(dic)

# 合并两个字典
# extend -- list
# update -- dict
# dic2 = {"age": 18}
# dic.update(dic2)
# print(dic)

# 5.2.4 查
# dic = {"name": "小明", "age":18}
# print(dic["name"])
# # print(dic["name2"])
# print(dic.get("name3", "不在"))  # 推荐用get

# 5.2.5 其他操作
# dic = {"name": "小明", "age":18}
# print(dic.keys())
# print(type(dic.keys()))
# for v in dic.keys():
#     print(v)
#
# print(dic.values())
# print(dic.items())
# print(type(dic.items()))  # [(k1,v1),(k2,v2),...]
# for k,v in dic.items():
#     print(k, "  ", v)


# 解构
# a, b = 1,2
# print(a)
# print(b)

# e, f,  = [1,2,3]
# print(e)
# print(f)
# print(d)

# dict嵌套
# dic = {"2f":{1:"hash"}, "st":[56]}
# print(dic)
# print(dic["2f"][1])
# print(dic.get("2ffas"))

"""
练习:
    dic2 = {
     'name':['fujing',2,3,5],
     'job':'teacher',
     'content':{'pytest':['python1','python2',100]}
     }
    1，将name对应的列表追加⼀个元素'wushu’。
    2，将name对应的列表中的fujing⾸字⺟⼤写。
    3，content对应的字典里加⼀个键值对  ’课程’：’linux’。
    4，将content对应的字典中的pytest对应的列表中的python2删除。
"""
dic2 = {
    'name': ['fujing', 2, 3, 5],
    'job': 'teacher',
    'content': {'pytest': ['python1', 'python2', 100]}
}

dic2["name"].append("wushu")
print(dic2)
# dic2.get("name")[0].title()
dic2.get("name")[0] = dic2.get("name")[0].capitalize()  #  注意字符串不可变
print(dic2)
# 3，content对应的字典里加⼀个键值对  ’课程’：’linux’。
dic2.get("content")["课程"] = "linux"
print(dic2)
# 4，将content对应的字典中的pytest对应的列表中的python2删除（用两种方法）。
# dic2.get("content").get("pytest").pop(1)
dic2.get("content").get("pytest").remove("python2")
print(dic2)



# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
# if a > b > c:
#     print(a, b, c)
# elif a > b and b < c:
#     a, b, c = a, c, b
#     print(a, b, c)
# elif a < b < c:
#     a, b, c = c, b, a
#     print(a, b, c)
# elif a < b and b > c:
#     if a > c:
#         a, b, c = b, a, c
#     else:
#         a, b, c = b, c, a
#     print(a, b, c)
# else:
#     print(a, b, c)