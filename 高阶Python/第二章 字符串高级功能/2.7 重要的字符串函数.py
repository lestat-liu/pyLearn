'''
    input(prompt_str)    #  提示用户输入字符串
    len(str)             #  返回字符串中字符个数，（包含空格）
    max(str)             #  返回字符串中编码最大的字符
    min(str)             #  返回字符串中编码最小的字符
    reversed(str)        #  返回一个字符串逆序的迭代器
    sorted(str)          #  返回一个按字符编码排序的字符数组
'''
print(len("he l l"))
print(max("he l l"))
print(min("hell"))
st = "hellworld"
st1 = reversed(st)
st2 = sorted(st)
print(st1)
for v in st:
    print(v, end="  ")
print()
print(st2)




