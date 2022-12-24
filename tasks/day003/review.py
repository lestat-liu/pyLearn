# -*- coding:utf-8 -*-
"""
@author: xcld
@file: review.py
@time: 2022-12-20 14:31
"""
# # 知识点回顾
# 1. 列表
#   - 列表的增删改查
# ```python

# 1.2 列表的索引和切片

lit = [1, 3, 5, 7, "hello world", [100, 99, 55], (2, 4, 6), {"d": 4, "K": 5}]
for show in lit:
    print(show)
# for i in len(lit):
#     print(i)
print("索引和切片")
print(
    f"lit[2]:{lit[2]}\nlit[2:]:{lit[2:]}\nlit[:2]:{lit[:2]}\nlit[1:3]:{lit[1:3]}\nlit[2:6:2]:{lit[2:6:2]}\nlit[-2]:{lit[-2]}\n")
print(f"lit[-4][:2]:{lit[-4][:2]}\n")  # 切片分片
print(f"lit[-4][1]:{lit[-4][1]}\n")
first, *rest = [1, 2, 3, 4, 5, 6]
print(first, rest)


def product(a, b, c):
    return a * b * c


L = [2, 5, 4]
print(f"product(*L):{product(*L)}\n")
print(f"product(2,*L[1:]):{product(2, *L[1:])}\n")

# 1.3 列表的增删改查

lst = [4, 5, 7, 2, 1, 3, 9, 6, 8, "番薯"]
print(f"lst:{lst}\n")
lst.insert(-1, "萝卜生")  # 将萝卜生插入到-1的位置
print(lst)
# lst.index("7", 1, 4)
K = lst[:9]
K.sort()
print(f"sort():{K}")
K.sort(reverse=True)
print(f"sort(reverse=True):{K}")
K.reverse()
print(f"K.reverse():{K}")
lst2 = ["咸鱼", "豆豉", "榄角", "姜"]
lst.extend(lst2)  # 将lst2追加的lst结尾 等价于 +=
print(f"lst:{lst}")

# 1.3.2  删--pop；remove；clear；del

lst.pop()  # 默认删除队尾即最右边的元素
print(f"pop():{lst}")
lst.pop(0)  # 删除索引位置的元素
print(f"pop(0):{lst}")
lst.remove("咸鱼")
print(f"remove(\"咸鱼\"):{lst}")  # 按元素内容删
# lst.remove(10)  # lst.remove(10) ValueError: list.remove(x): x not in list 报错退出
# print(f"remove(10):{lst}")

# lst.clear()  # 清空列表
# print(f"clear():{lst}")

# del lst[1:2] # 不知道怎么用，输出结果 不对
# print(f"del lst[1:2]:{lst}")

# 1.3.3 改--lst[2]=str

# lst[-5] = "木瓜生"
lst[9] = "木瓜生"
print(f"lst[9]:{lst}")
lst[10:] = ["鲍鱼", "龙虾"]
print(f"lst[10:]:{lst}")

# 1.3.4 查--for循环

CC = [1, 1, 1, 5, 5, 6, 2]
print(CC)
print(f"CC.count(1):{CC.count(1)}")

for H in lst:
    print(H, end=" ")

for index, H in enumerate(lst):
    print(" index: ", index, "H: ", H)

# 2. 元组和元组的嵌套
## 元组定义

tup = (1, 3, 5, 7, {"h": 89, "i": 90}, [1, 2, 3, 4, 5], (5, 6, 7, 8, (9, 10, 11, 12)))
print(tup)
I = list(tup)
print(I)
J = tuple(I)
print(J)
connect = tup[:4] + J
print(connect)

# 索引和切片
# 和列表类似跳过

# count、index、len

Q = tup.count(1)
print(f"tup.count(1):{Q}")
R = tup[6][4].index(11)
print(f"tup.count(1):{R}")

# 3. range
for S in range(1, 15, 2):
    print(f"range(1,15,2):{S}")
    print()
for T in range(15, 1, -2):
    print(f"range(15,1,-2):{T}")

# 4. 字典
'''
在dict中key是唯⼀的(可哈希). 在保存的时候, 根据key来计算出⼀个内存地址. 然后将key-value保存在这个地址中.
已知的可哈希(不可变)的数据类型: int, str, tuple, bool
不可哈希(可变)的数据类型: list, dict, set
'''
Dic = {"Fist": 67, "Select": "select hello from K", "Sale": "True","Source": "[78,98,63,45,21]"}
#  key相同，后面的会覆盖前面的value
print(f"Dic:{Dic}")

#    - 字典的增删改查
# 增
Dic1 = Dic.copy()  # Dic 的浅拷贝
print(f"Dic1:{Dic1}")
Dic["Order"] = "(1,2,3,4,5)"
print(f"Dic:{Dic}")

#    - 字典的嵌套
# 5. 集合
# Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。
#  ![img.png](img.png)
#    - 集合增删改查
#    ```Python
# # 创建集合的字面量语法
# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
# print('Length =', len(set1))
# # 创建集合的构造器语法(面向对象部分会进行详细讲解)
# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 2, 1))
# print(set2, set3)
# # 创建集合的推导式语法(推导式也可以用于推导集合)
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)
# ```
#
# 向集合添加元素和从集合删除元素。
#
# ```Python
# set1.add(4)
# set1.add(5)
# set2.update([11, 12])
# set2.discard(5)
# if 4 in set2:
#     set2.remove(4)
# print(set1, set2)
# print(set3.pop())
# print(set3)
# ```
#    - 集合运算
# 集合的成员、交集、并集、差集等运算。
#
# ```Python
# # 集合的交集、并集、差集、对称差运算
# print(set1 & set2)
# # print(set1.intersection(set2))
# print(set1 | set2)
# # print(set1.union(set2))
# print(set1 - set2)
# # print(set1.difference(set2))
# print(set1 ^ set2)
# # print(set1.symmetric_difference(set2))
# # 判断子集和超集
# print(set2 <= set1)
# # print(set2.issubset(set1))
# print(set3 <= set1)
# # print(set3.issubset(set1))
# print(set1 >= set2)
# # print(set1.issuperset(set2))
# print(set1 >= set3)
# # print(set1.issuperset(set3))
# ```
