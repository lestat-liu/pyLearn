
'''
运算符语法         说明
name = str         将字符串赋值给指定变量
str1 == str2       当str1和str2内容相同，返回True，否则返回False，大小写敏感
str1 != str2       当str1和str2内容不相同时，返回True
str1 < str2        按字母表顺序比较：如："abc" < "def" ,True; "abc" < "aaa" ,False
str1 > str2        效果类似上面
str1 <= str2       str1与str2按字母表顺序比较，在前或者内容相同时，返回True
str1 >= str2       str1与str2按字母表顺序比较，在后或者内容相同时，返回True
str1 + str2        把str2追加到str1后面
str1 * n           n为一个整数，就是连接n次的自身字符串
n * str1           同上一条
str1 in str2       若str1整体包含在str2,则返回True
str1 not in str2   若str1整体不包含在str2,则返回True，区分大小写
str is obj         若str与obj指向同一个内存对象，则返回True；用于字符串与None或未知类型对象的比较很有用
str is not obj     str与obj指向不同的内存对象，则返回True

None是唯一的，因此适合使用is进行测试
'''


st1 = "hello world!"
st2 = "hello world!"
print(st1 == st2)
print(id(st1))
print(id(st2))
print(st1 is st2)