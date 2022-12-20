# 1、格式化输出
'''
    1、%s
    2、format
    3、f""
'''
# st = input("请输入你的名字")
# # st = "小明"
# print("我叫：%s" % st)
# print("欢迎你：%s", st)  # 相当于字符串拼接

# st = input("请输入你的名字")
# st3 = input("请输入你的名字")
#
# # st2 = "你好{}".format(st)
#
# st5 = "你好{1},  wo好{0} ".format(st, st3)
# print(st5)

# name = "xiaobai"
# st6 = f"好{name}"
# print(st6)


# 2、基本运算符
#     算数运算、
#     ⽐较运算、
#     逻辑运算、
#     赋值运算、
#     成员运算、
#     身份运算、
#     位运算.

# 2.1 算数运算
'''
    +  
    -
    *
    /
    %
    **
    //
'''
# x = 9
# y = 2
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x**y)
# print(x//y)


# 2.2 ⽐较运算
'''
    ==与is
    ==判断值是否相等
    is: a is b 判断地址是否一样
    !=
    <> 
    >
    <
    >=
    <=
'''
# a = 1
# b = 1
# if a == b:
#     print("a等于b")
# else:
#     print("a不等于b")



# a = 2
# b = 2
# # 小数池 0-255
# if a is b:
#     print("ab在小数池里面")

# 待查找小数池的范围
# c = 3000
# d = 3000
# if c is d:
#     print("cd不在小数池里面")


# 2.3 赋值运算  主要用于数值类型
''' 
    =
    +=
    -=
    *=
    /=
    %=
    **=
    //=
'''
# a = 12
# a += 1  # 等效于  a = a + 1
# print(a)

# a = "hello "
# b = "world! "
# print(a+b)
# print(a * 5)


# 2.3 算术逻辑运算符
'''
    and
    or
    not
    优先级：
    ()>not>and>or
'''
# bool_1 = 5 > 4 or 1 < 3 and 1 == 1 and not 5
# print(bool_1)


# 3、基本的数据类型
'''
⼀.python基本数据类型
    1. int ==> 整数. 主要⽤来进⾏数学运算
    2. str ==> 字符串, 可以保存少量数据并进⾏相应的操作
    3. bool==>判断真假, True 1, False  0
    4. list==> 存储⼤量数据.⽤[ ]表⽰
    5. tuple=> 元组, 不可以发⽣改变 ⽤( )表⽰
    6. dict==> 字典, 保存键值对, ⼀样可以保存⼤量数据
    7. set==> 集合, 保存⼤量数据. 不可以重复. 其实就是不保存value的dict
'''

# 3.1 整数(int)
# a = 10
# b = int("0001", base=2)
# print(b)

# 3.2 布尔值(bool)
# true            false
#   1, "st"         "", 0 [] {} ()

# 3.3 字符串(str)
# "ff" 'fad'  '''ffsda'''  """fsdf"""

# 3.3.1 切片和索引
# st = "python"
# st1 = st[0:2]
# st2 = st[2:4]
# print(st1)
# print("st2 ", st2)
#
# print(st[-1])
# print(st[-2])
# print(st[2])
# # print(st[6])

# st = "python golang"
# st3 = st[0:13:2]  # 步长
# print(st3)

# 3.3.2 大小写转换
# st1 = "andfsa"
# st2 = "ADF"
# print(st1.capitalize())
# print(st1.upper())
# print(st2.lower())

# st = "abc"
# print(st * 5)

# 去空格
# username = "   ad  d  "
# username3 = username.strip()
# username1 = username.lstrip()
# username2 = username.rstrip()
# print(username3)
# print(username1)
# print(username2)

# lis = username.split(" ")
# print(lis)
# st6 = " ".join(lis)
# print(st6)



# name2 = "xiaoming"
# name2 = name2.replace("m", "M")
# print(name2)
# name2[0] = "X"  TypeError: 'str' object does not support item assignment

# 查找：
# in       not in
# user = input("请输入内容：")
# if "py" in user:
#     print("这是Python")
# else:
#     print("不在")

# 长度
# st = "fasdfasdgasgashgg"
# print("st的长度是：%s" % len(st))
# print("st的长度是：{}".format(len(st)))

# lst = [1, 2, 2, 5,]
# print(len(lst))

# 查找字符或字符串出现的次数
# st = "afdasdfaa fafdaaa"
# ret = st.count("a")
# print(ret)
#
# ret2 = st.count('af ')
# print(ret2)

# 字符或者字符串第一次出现的下标位置
# st = "afdasdfaa fafdaaa"
# ret2 = st.find("fa")
# print(ret2)


# st = "abcd"
# for v in st:
#     print(v, end=" ")



#  打印ASCII码
char = input("请输入一个字符：")
char2 = input("请输入一个整数：")
print(char + " 对应的ASCII码是： " , ord(char))
print(char2 + " 对应的ASCII码是： ", chr(int(char2)))
