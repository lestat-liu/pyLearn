# repr会原样输出
test_str = "Here is a \n newline!"
print(test_str)
print(str(test_str))
print(repr(test_str))

# !r修饰符会调用rper函数
print("{!r}".format(test_str))

# !r与position字段组合使用
print("{1!r} love {0!r}".format("小红", "小明"))


