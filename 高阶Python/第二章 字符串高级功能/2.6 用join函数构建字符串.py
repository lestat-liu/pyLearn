
'''
    用join函数通常比字符串连接操作更高效，+会在每次在内存中创建全新的字符串

'''

n = ord("A")
a_lst = []
for i in range(n, n+26):
    a_lst.append(chr(i))

s = "".join(a_lst)  #  使用join将列表的全部元素连接成字符串
print(s)

