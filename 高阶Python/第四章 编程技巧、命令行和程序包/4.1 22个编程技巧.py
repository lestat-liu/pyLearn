
# 1、多行字符串
# st = "aa发f"  " "\
#      "aaf"\
#      "ff"
# print(st)

# 2、合理使用for循环
# beat_list = ["John", "Paul", "George", "Ringo"]
# for guy in beat_list:
#     print(guy)
#
# # 或者用enumerate来获取值和索引
# for i, name in enumerate(beat_list, 1):  # 指定索引从1开始
#     print(i, ". ",  name)
# print(beat_list)


# 3、使用组合运算符(+=、*=等等)
"""
    首先：任何赋值运算符优先级都比较低，通常最后执行
    其次：赋值运算符能否就地修改，取决于被操作对象的类型是否可变。
"""
# s1 = s2 = "fff"
# s1 += 'sds'
# print("s1: ", s1)
# print("s2: ", s2)
#
# a_list = b_list = [10, 20]
# a_list += [30, 40]
# print("a_list:  ", a_list)
# print("b_list:  ", b_list)


# 5、元组赋值
# a = 1
# b = 2
# a, b = b, a
# print("a: ", a)
# print("b: ", b)


# 6、使用高级元组赋值
# tup = 10,20,30
# a, b, c = tup
# print(a, b, c)
#
# d, *e = 1,2,3,4
# print(d,  "  ", e)
#
# f, *g, h = 6,4,7,8,9,1
# print(f, "  ", g, "  ", h)

# 7、列表和字符串的“乘法”
# my_list = [12] * 1000
# print(my_list)
# print(len(my_list))

# div_str = "_" * 40
# print(div_str)


# 8、返回多个值
# def quad(a,b,c):
#     return a+b, a+c
#
# x1, x2 = quad(1,2,3)
# print(x1)
# print(x2)
# x = quad(1,2,3)
# print(x)  # (3, 4)返回一个元组


# 9、使用循环和else关键字
# def find_divisor(n, max):
#     for i in range(2, max+1):
#         if n % i == 0:
#             print(i, "  可以整除 ", max)
#             break  # 一定要跳出循环，不然else一定会被执行
#     else:  #  while循环也可以用
#         print("不能被整除")
#
# find_divisor(49, 6)
# find_divisor(49, 7)


# 10、使用布尔值和not运算
"""
    所有的空集合、特殊值None，都是False；
"""
# not 判断是否为空


# 11、将字符串视为字符列表
# test_str = input("请输入字符串")
# a_list = [c for c in test_str]
# print(a_list)

# 12、使用replace方法消除字符
# st = "fa fsdf  fasfd f   "
# st = st.replace(" ", "")
# print(st)


# 13、使用内置函数，不写不必要的循环
# def calc_triangle_num(n):
#     return sum(range(n+1))
#
# print(calc_triangle_num(100))


# 14、使用链式比较: (n < x < m)
# if 0 < x  < 100:


# 15、用函数列表模拟switch语句
# def a():
#     print("AAAAAAAA")
# def b():
#     print("bbbbbbbb")
#
# n = 2
# fn = [a, b][n-1]  # 法一：
# fn()
#
# menu_dict = {'aa':a, "bb":b}  #  法二：
# menu_dict.get("aa")()


# 16、正确使用is运算符
'''
    ==    用于判断值是否相同
    is    用于判断是否为同一对象，如：None，True，False这些正在内存中是唯一对象
'''
# a_value = False
# print(a_value)
# # if a_value is None:
# if  a_value is False:
#     print("a_value is None")

# 17、单行for循环
# for i in range(10): print(i, end=" ")


# 18、使用分号，将多条语句强制压缩到一行
# a = 1; b = 2; c = a + b; print(c)


# 19、编写单行的if/then/else语句
'''
    true_expr if conditional else false_expr
    {conditional}为true，则执行true_expr并返回；否则执行false_expr并返回。
'''
# a = 1
# cell = "a=1条件成立" if a == 1 else "条件不成立"
# print(cell)

# 20、使用range函数来创建枚举值

# red, blue, green, black, white = range(5)
# red, blue, green, black, white = range(1,6)
# print(red)
# print(blue)
# print(white)


# 导入枚举类
from enum import Enum


# 继承枚举类
class color(Enum):
    YELLOW = 1
    BEOWN = 1
    # 注意BROWN的值和YELLOW的值相同，这是允许的，此时的BROWN相当于YELLOW的别名
    RED = 2
    GREEN = 3
    PINK = 4


class color2(Enum):
    YELLOW = 1
    RED = 2
    GREEN = 3
    PINK = 4


# print(color.YELLOW)  # color.YELLOW
# print(type(color.YELLOW))  # <enum 'color'>
#
# print(color.YELLOW.value)  # 1
# print(type(color.YELLOW.value))  # <class 'int'>
#
# print(color.YELLOW == 1)  # False
# print(color.YELLOW.value == 1)  # True
# print(color.YELLOW == color.YELLOW)  # True
# print(color.YELLOW == color2.YELLOW)  # False
# print(color.YELLOW is color2.YELLOW)  # False
# print(color.YELLOW is color.YELLOW)  # True
#
# print(color(1))  # color.YELLOW
# print(type(color(1)))  # <enum 'color'>
'''
注意事项如下：
    1、枚举类不能用来实例化对象
    
    2、访问枚举类中的某一项，直接使用类名访问加上要访问的项即可，比如 color.YELLOW
    
    3、枚举类里面定义的Key = Value，在类外部不能修改Value值，也就是说下面这个做法是错误的
    
    4、枚举项可以用来比较，使用==，或者is
    
    5、导入Enum之后，一个枚举类中的Key和Value，Key不能相同，Value可以相，但是Value相同的各项Key都会当做别名，
    
    6、如果要枚举类中的Value只能是整型数字，那么，可以导入IntEnum，然后继承IntEnum即可，注意，此时，如果value为字符串的数字，也不会报错：
    from enum import IntEnum

    7、如果要枚举类中的key也不能相同，那么在导入Enum的同时，需要导入unique函数
    from enum import Enum, unique

'''


# 21、减少print函数的使用
# 法一：预先组装好一个多行字符再输出
# row_of_asterisks = "*" * 40
# s = ""
# for i in range(20):
#     s += row_of_asterisks + "\n"
#
# print(s)


# 法二：
# print("\n".join(["*" * 40] * 20))


# 22、使用下划线分隔大数字，方便阅读，不影响输入输出
'''
    ①、不能连续使用两个下划线
    ②、不能放在数字的开头或结尾，开头则会被视为变量名
    ③、可以在小数点的任意一侧
'''
num = 15_50_1
print(num)









