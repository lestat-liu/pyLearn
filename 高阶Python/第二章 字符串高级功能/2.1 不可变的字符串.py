'''

    python中的数据类型分为：
        可变的----可以“就地”更改
        不可变的---无法“就地”更改
'''
my_str = "hell world!"
# my_str[0] = "H"   # TypeError: 'str' object does not support item assignment

my_str = "HELLO world!"   #  这是因为变量只是一个名称，可以反复使用，
print(my_str)             #  这里没有违反字符串的不可变性，而是依次把两个不同的字符串赋值给my_str
