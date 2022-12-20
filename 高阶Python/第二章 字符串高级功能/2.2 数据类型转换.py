
# 1、普通转换
s = "45"
n = int(s)
x = float(s)
print(n)
print(x)


# 2、int转换可以接受可选的第二个参数
n1 = int("10001", 2)  #  将二进制字符串转换成十进制的数字
n2 = int("775", 8)  #  将八进制字符串转换成十进制的数字
n3 = int("1E", 16)  #  将十六进制字符串转换成十进制的数字
print("二进制 10001 转十进制", n1)
print("八进制 775 转十进制", n2)
print("十六进制 1E 转十进制", n3)


# 3、数字转ASCII码、Unicode码
num = ord("a")  # ASCII码转数字
print(num)

num2 = chr(98)  # 数字转ASCII码
print(num2)
