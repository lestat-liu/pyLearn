'''
作用：
    用来实现数字与字符的转换，与ASCII或者Unicode编码的字符对应

    ord(str)    返回字符的数字编码，字符长度必须为1，
    chr(n)      将ASCII/Unicode编码转换成一个字符

'''
print(ord("a"))
print(chr(98))

# 1、in和not in运算符支持长度大于1的字符串，但经常用单字符判断
#     测试字符串的第一个字符是否为元音,还是辅音
s = "elephant"
if s[0] in "aeiou":
    print("First char. is a vowel.")
else:
    print("First char. is a consonant")

#  优化加上判断大小写,三种写法都可
if s[0] in "aeiouAEIOU":
# if s[0].lower() in "aeiou":
# if s[0].upper() in "AEIOU":
    print("First char. is a vowel.")
else:
    print("First char. is a consonant")
