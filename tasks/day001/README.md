# Day1作业及默写
---

### 1、简述变量量命名规范
- 字母、下划线等
- 不能数字开头或纯数字
- 驼峰命名
- 命名区分大小写
- 不能用内置关键字命名

### 2、 name = input(“>>>”) name变量是什什么数据类型？
- ~~字符串类型~~ 
- 错误

- 点评：
    是字符串类型
```python
name = input(">> > ")
print(type(name))
# >> > fas 
# # <class 'str'>
```
### 3.if条件语句句的基本结构？
三种结构：
1. 条件动作
```python
if boolean_expression1:
    suite1
```
2. 分支型
```python
if boolean_expression1:
    suite1
else
    else_suite
```
3. 多分支
```python
if boolean_expression1:
    suite1
elif boolean_expression2:
    suite2
elif boolean_expressionN:
    suiteN
else:
    else_suite
```

### 4.用print打印出下⾯面内容：
文能提笔安天下,
武能上马定乾坤.
心存谋略略何人胜,
古今英雄唯是君.

```python
list=["文能提笔安天下,","武能上马定乾坤.","心存谋略略何人胜,","古今英雄唯是君."]
for Element in list:
    print(Element)
```
###  5.利用if语句写出猜大小的游戏：
设定一个理理想数字比如： 66，让用户输入数字，如果比66⼤大，则显示猜测
的结果大了了；如果比66小，则显示猜测的结果小了了;只有等于66，显示猜测结果
正确。
```python
Num = int(input("请输入一个整数："))
if Num > 66:
    print("这个整数比66要大！")
elif Num < 66:
    print("这个整数比66要小！")
else:
    print("这个数和66相等！")
```
- 批改
```python
Num = int(input("请输入一个整数："))
while 1:
    if Num > 66:
        print("这个整数比66要大！")
    elif Num < 66:
        print("这个整数比66要小！")
    else:
        print("这个数和66相等！")
        break

```

### 6.提⽰⽤用户输⼊入他的年年龄, 程序进⾏行行判断.
如果小于10, 提⽰⼩小屁孩, 如果⼤大于10, ⼩小于 20, 提⽰⻘青春期叛逆的⼩小屁孩.
如果大于20, ⼩小于30. 提⽰开始定性, 开始混社会的⼩小 屁孩⼉儿, 如果⼤大于30, ⼩小于
40. 提⽰看⽼老老⼤大不不⼩小了了, 赶紧结婚⼩小屁孩⼉儿. 如果⼤大于40, ⼩小 于50. 提⽰家⾥里里有个
不不听话的⼩小屁孩⼉儿. 如果⼤大于50, ⼩小于60. 提⽰⾃自⼰己⻢马上变成不不听 话的⽼老老屁孩⼉儿.
如果⼤大于60, ⼩小于70. 提⽰活着还不不错的⽼老老屁孩⼉儿. 如果⼤大于70, ⼩小于 90. 提⽰⼈人
⽣生就快结束了了的⼀一个⽼老老屁孩⼉儿. 如果⼤大于90以上. 提⽰. 再⻅见了了这个世界.
```python
Age = int(input("请输入他的年龄："))
if Age < 10:
    print("小屁孩！")
elif 10 < Age < 20:
    print("青春期叛逆的小屁孩！")
elif 20 < Age < 30:
    print("开始混社会的小屁孩儿！")
elif 30 < Age < 40:
    print("看老大不不小了了, 赶紧结婚小屁孩儿！")
elif 40 < Age < 50:
    print("家里有个不不听话的小屁孩儿！")
elif 50 < Age < 60:
    print("马上变成不听话的老屁孩儿！")
elif 60 < Age < 70:
    print("活着不错的老屁孩儿！")
elif 70 < Age < 90:
    print("安享晚年的老屁孩儿！")
else:
    print("曾经有份针织的爱情摆在我面面，我妹有珍惜，直到……算了活明白了！")
```
### 7、单行注释以及多行注释？
1. 单行注释
 - 选中单行 使用ctrl +/ 注释
2. 多行注释
 - 框选多行，使用ctrl +/ 注释
 - 或者用三个单引号首位注释代码段

### 8、提⽰⽤户输⼊⿇花藤. 判断⽤户输⼊的对不对. 如果对, 提⽰真聪明, 如果不
对, 提⽰你是大聪明

```python
Iput = str(input("请输麻花藤！："))
Com = "麻花藤"
if Iput == Com:
    print("你真聪明！")
else:
    print("你是大聪明！")
```
### 9. 用户输入一个月份. 然后判断月份是多少月 . 根据不同的月份, 打印出不同的
饮食(根据个人习惯和老家习惯随意编写)
```python
Month = int(input("请输入一个月份数（1-12月）："))
if 1 < Month < 3:
    print("春天，三月枇杷，等吃枇杷！")
elif 4 < Month < 6:
    print("夏天，四月李，等吃李！")
elif 6 < Month < 8:
    print("夏天，喝酒！吃粽子！")
elif 9 < Month < 10:
    print("秋天，看着来吃！")
elif 10 < Month < 12:
    print("冬天，打火锅！")
else:
    print("你输错了！")
```
10. 用户输入一个分数. 根据分数来判断用户考试成绩的档次,
```
>=90 A
>=80 B
>=70 C
>=60 D
< 60 E
```
```python
Score = float(input("请输入一个分数（成绩）："))
if Score >= 90:
    print("你的得分评为A！")
elif Score >= 80:
    print("你的得分评为B！")
elif Score >= 70:
    print("你的得分评为C！")
elif Score >= 60:
    print("你的得分评为D！")
else:
    print("你的得分评为E！")
```

明日默写代码：
1.变量量的命名规范。
2.单行行注释，多行行注释。
