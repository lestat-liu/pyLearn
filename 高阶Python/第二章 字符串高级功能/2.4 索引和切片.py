
'''
string[beg: end]        从beg开始到end（不包含）的字符串
string[: end]           从开头开始到end（不包含）的字符串
string[beg: ]           从开beg一直到结尾的字符串
string[: ]              复制原字符串
string[beg: end: step]  从beg到end（不包含）的字符串，字符之间的索引间隔为step
'''

# 1、使用正负索引，插头去尾一个字符
king_str = '"Henry VIII"'
print(king_str)
new_str = king_str[1:-1]
print(new_str)


# 2、字符串切片的步长，默认为1，我们也可以设置负数的-1的步长
a_str = "RoboCop"
print(a_str[1::2])  #  从索引1开始切片，步长为2   ooo
print(a_str[::-2])  # 从后往前切片，步长为2     pCbR


