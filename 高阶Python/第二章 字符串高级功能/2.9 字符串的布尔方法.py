
'''
       方法名                             返回True的条件
    str.isalnum()         所有字符都是字母或者数字，并且至少包含一个字符
    str.isalpha()         所有字符都是字母，并且至少包含一个字符
    str.isdeciaml()       所有的字符都是十进制数，并且至少有一个字符。该方法和isdigit类似，一般用于Unicode编码字符
    str.isdigit()         所有的字符都是十进制数，并且至少有一个字符。
    str.isidentifier()    该字符串包含有效的Python标识符。第一个字符必须是字母或下划线。其他字母必须是字母、下划线或数字。
    str.islower()         字符串中所有字母均为小写，且至少有一个字母。
    str.isupper()         字符串中所有的字母均为大写，且至少有一个字母。
    str.isprintable()     字符串中的所有字符（若有）都是可以打印字符。不包括特殊字符，如：\n和\t
    str.isspace()         字符串中的所有字符均为“空白”字符，且至少有一个字符。
    str.istitle()         字符串中每个词都是有效的标题，至少一个字符。每个单词的首字母大写，且其他字母小写。单词间有空白和标点符号、

'''

h_str = "Hello"
if h_str[0].isupper():
    print("全部字母都是大写 ", h_str[0])

if h_str.isupper():
    print("全部字母都是大写： ", h_str)
else:
    print("字符串不是全部大写： ", h_str)


