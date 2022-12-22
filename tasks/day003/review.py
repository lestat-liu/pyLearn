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
print(f"lit[-4][:2]:{lit[-4][:2]}\n")
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
lst2 = ["咸鱼", "豆豉", "榄角", "姜"]
lst.extend(lst2)  # 将lst2追加的lst结尾 等价于 +=
print(lst)

#   - 列表的嵌套
# 2. 元组和元组的嵌套
# 3. range
# 4. 字典
#    - 字典的增删改查
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
