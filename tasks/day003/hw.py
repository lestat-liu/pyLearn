# -*- coding:utf-8 -*-
"""
@author: xcld
@file: hw.py
@time: 2022-12-26 17:08
"""
# 1题
# li = ["lex", "WuSi", "ruantian", "barry", "wenzhou"]
# print("1.1 li长度为：", len(li))
# li.append('seven')
# print("2)列表中追加元素' seven ',并输出添加后的列表li:", li)
# li.insert(0, 'Tony')
# print("3)请在列表的第1个位置插⼊元素Tony,并输出添加后的列表:", li)
# li.insert(1, 'kelly')
# print("4)请在列表的第2个位置插⼊元素kelly,并输出添加后的列表:", li)
# print("5)……每⼀个元素添加到列表li中，⼀⾏代码实现，不允许循环添加:", li + [1,"a",3,4,"heart"])
# # s = "qwert"
# # li.extend(s)
# # print(li)
# print("6)请将字符串s = qwert 的每⼀个元素添加到列表li中，⼀⾏代码实现，不允许循环添加。:", li + list({}.fromkeys("qwert").keys()))
# li.remove("lex")
# print("7)请删除列表中的元素\"eric\"(这里搞错了吧，我随便删一个比如lex吧),并输出添加后的列表:", li)
# li.pop(1)
# print("8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表:", li)
# del li[1:4]
# print("9)请删除列表中的第2⾄4个元素，并输出删除元素后的列表:", li)
# li.reverse()
# print("10)请将列表所有得元素反转，并输出反转后的列表:", li)
# # print(":",)
# print("11)请计算出\"seven\"元素在列表li中出现的次数，并输出该次数。:", li.count("seven"))

# 2题

# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# print("1)通过对li列表的切⽚形成新的列表l1,l1 = [1,3,2]:", li[:3])
# # print(":",)
# print("2)通过对li列表的切⽚形成新的列表l2,l2 = [\"a\",4,\"b\"]:", li[3:6])
# l3 = li[:3] + li[3:7]
# l3.remove("a")
# l3.remove("b")
# l3.remove(3)
# # l3 = filter(str.isdigit, [list(ll) for ll in li])
# print("3)通过对li列表的切⽚形成新的列表l3,l3 = [\"1,2,4,5]:", l3)
# l4  =  []
# l4.append(li[1])
# l4.append(li[3])
# l4.append(li[5])
# print("4)通过对li列表的切⽚形成新的列表l4,l4 = [3,'a','b']:", l4)
# l5 = list(li[-1])
# print("5)通过对li列表的切⽚形成新的列表l5,l5 = [\"c\"]:", l5)
# l4.reverse()
# l6 = l4
# print("6)通过对li列表的切⽚形成新的列表l6,l6 = [\"b\",\"a\",3]:", l6)

# 3题

# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lst = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [11, 22, 33]]
lis1 = [j for i in lst for j in i]
print(lis1)
# print("1)将列表lis中的\"tt\"变成⼤写（⽤两种⽅式）:", lis[3][2][1][0].upper())
# print(":",)

