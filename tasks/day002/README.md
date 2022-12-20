# day002 作业

---

### 1、判断下列逻辑语句的True,False.
#### 1）1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
#### 2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
```
1) true ,4 > 5 and 2 > 1 and 9 > 8==> false   1 > 1 or 3 < 4 or false ==> true or 7 < 6
==> true

2) false ,not 2 > 1 and 3 < 4 ==> false or 4 > 5 and 2 > 1 and 9 > 8 ==> false or 7 < 6 ==>false 

```

### 2、求出下列逻辑语句的值。
- 1),8 or 3 and 4 or 2 and 0 or 9 and 7
- 2),0 or 2 and 3 and 4 or 6 and 0 or 3

```
1) true ,8 or true or false or true ==> true 
2) true, 0 or true or false or 3 ==> true 
```


### 3、下列结果是什么？
- 1)、6 or 2 > 1
- 2)、3 or 2 > 1
- 3)、0 or 5 < 4
- 4)、5 < 4 or 3
- 5)、2 > 1 or 6
- 6)、3 and 2 > 1
- 7)、0 and 3 > 1
- 8)、2 > 1 and 3
- 9)、3 > 1 and 0
- 10)、3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
```
1) true , 6 or true ==> true 
2) true ,3 or true ==> true 
3) false , 0 or false ==>false
4) true , false or 3 ==>true
5) true , true or 6 ==> true
6) true, 3 and true ==> true
7) false, 0 and true ==> false
8) true, true and 3 ==> true
9) false, true and 0 ==>false
10) true , 3 > 1 and 2 ==> true or 2 < 3 and 3 and 4 ==> true or true ==> true

```


### 4、利⽤while语句写出猜⼤⼩的游戏：
设定⼀个理想数字⽐如：66，让⽤户输⼊数字，如果⽐66⼤，则显示猜测
的结果⼤了；如果⽐66⼩，则显示猜测的结果⼩了;只有等于66，显示猜测结果
正确，然后退出循环。
```python
# -*- coding:utf-8 -*-
"""
@author: xcld
@file: day002_hw.py
@time: 2022-12-07 12:01
"""
Num = int(input("请输入一个要猜测的数字："))
Sum = 1
while Sum > 0:
    if Num > 66:
        print('猜测的结果:{} 大了!'.format(Num))
    elif Num < 66:
        print('猜测的结果:{} 小了!'.format(Num))
    else:
        print('猜测结果是:{} 正确！'.format(Num))
    Sum -= 1 #Python没有自增自减

```
- 批改
```python
# 题目意思是，让用户一直尝试，知道输入正确为止
while True:
    Num = int(input("请输入一个要猜测的数字："))
    if Num > 66:
        print('猜测的结果:{} 大了!'.format(Num))
    elif Num < 66:
        print('猜测的结果:{} 小了!'.format(Num))
    else:
        print('猜测结果是:{} 正确！'.format(Num))
        break
```

### 5、在上题的基础上进⾏升级：
给⽤户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循
环，如果三次之内没有猜测正确，则⾃动退出循环，并显示‘太笨了你....’。
```python
Sum = 3
# i = 1
# while i > 0:
while Sum > 0:
    Num = int(input("请输入一个要猜测的数字："))
    if Num > 66:
        print('猜测的结果:{} 大了!'.format(Num))
    elif Num < 66:
        print('猜测的结果:{} 小了!'.format(Num))
    elif Num == 66:
        print('猜测结果是:{} 正确！'.format(Num))
        break
    Sum -= 1
else:
        print("太笨了你！其实，我对你是有一些失望的。当初给你定级p7，是高于你面试时的水平的。\n我是希望进来后，你能够拼一把，快速成长起来的。p7这个层级，不是把事情做好就可以的。\n你需要有体系化思考的能力。你做的事情，他的价值点在哪里？你是否作出了壁垒，形成了核心竞争力？\n你做的事情，和公司内其他团队的差异化在哪里？你的事情，是否沉淀了一套可复用的物理资料和方法论？\n为什么是你来做，其他人不能做吗？你需要有自己的判断力，而不是我说什么你就做什么。\n后续，把你的思考沉淀到日报周报月报里，我希望看到你的思考，而不仅仅是进度。\n另外，提醒一下，你的产出，和同层级比，是有些单薄的，马上要到年底了，加把劲儿。\n你看咱们团队的那个A, 人家去年晋升之前，可以一整年都在项目室打地铺的。\n成长，一定是伴随着痛苦的，当你最痛苦的时候其实才是你成长最快的时候。加油")
```

- 批改
```python
# 根据修改来，完成本题
```
### 6、⽤户输⼊⼀个数. 判断这个数是否是⼀个质数(升级题).
```python
from math import sqrt
n = int(input("请输入一个正整数："))
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            print(f"{n}这不是质数")
            # return False
        else:
            print(f"{n}是质数")
    # return True
#这题先放弃
```


### 7、输⼊⼀个⼴告标语. 判断这个⼴告是否合法. 根据最新的⼴告法来判断. ⼴
告法内容过多. 我们就判断是否包含'最', '第⼀', '稀缺', '国家级'等字样. 如果包
含. 提示, ⼴告不合法
  例如, 1. python世界第⼀. ==> 不合法
```python
Adv = input("请输入你认为牛逼的广告语：")
if Adv.count("最") or Adv.count("第一") or Adv.count("稀缺") or Adv.count("国家级"):
    print("广告语不合法！", Adv)
else:
    print("广告语很棒!", Adv)
```

- 批改：
```python
st = "heeeddd"
print(st.count("e"))   #  这里要统计e出现的次数，用在这里不合理，会降低效率

# 应该用in,只要出现一次就行;或者index只要出现一次就行
print("e" in st)
print(st.index("e"))
```

### 8、⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
```python
Sum = 3
Scr = "Ak123"
while Sum:
    Ipu = input("请输入密码：")
    if Ipu == Scr:
        print("密码输入正确!")
        break
    else:
        Sum -= 1
        print(f"请重新输入，还剩{Sum}次机会！")
```


### 9、有变量name = "aleX leNb" 完成如下操作：
- 1)移除 name 变量对应的值两边的空格,并输出处理结果
- 2)移除name变量左边的"al"并输出处理结果
- 3)移除name变量右⾯的"Nb",并输出处理结果
- 4)移除name变量开头的a"与最后的"b",并输出处理结果
- 5)判断 name 变量是否以 "al" 开头,并输出结果
- 6)判断name变量是否以"Nb"结尾,并输出结果
- 7)将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
- 8)将name变量对应的值中的第⼀个"l"替换成"p",并输出结果
- 9)将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
- 10)将name变量对应的值根据第⼀个"l"分割,并输出结果。
- 11)将 name 变量对应的值变⼤写,并输出结果
- 12)将 name 变量对应的值变⼩写,并输出结果
- 13)将name变量对应的值⾸字⺟"a"⼤写,并输出结果
- 14)判断name变量对应的值字⺟"l"出现⼏次，并输出结果
- 15)如果判断name变量对应的值前四位"l"出现⼏次,并输出结果
- 16)从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
- 17)从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1)输出结果
- 18)从name变量对应的值中找到"X le"对应的索引,并输出结果
- 19)请输出 name 变量对应的值的第 2 个字符?
- 20)请输出 name 变量对应的值的前 3 个字符?
- 21)请输出 name 变量对应的值的后 2 个字符?
- 22)请输出 name 变量对应的值中 "e" 所在索引位置?

```python
name = " aleX leNb "
print(name)
Rlsp = name.strip()
print(f"1):{Rlsp}")
print(f"2):{name[2:]}")
print(f"3):{name[:-3]}")
# print(f"4):{name[2:9]}")
Yc = Rlsp.strip('ab')
print(f"4):{Yc}")
Kt = name.startswith("al")
print(f"5):{Kt}")
Jw = name.endswith("Nb")
print(f"6):{Jw}")
Rep = name.replace("l", "p")
Rep1 = name.replace("l", "p", 1)
print(f"7):{Rep}")
print(f"8):{Rep1}")
Spl = name.split("l")
Spl1 = name.split("l", 1)
print(f"9):{Spl}")
print(f"10):{Spl1}")
Dx = name.upper()
Dx1 = name.lower()
Dx2 = Rlsp.capitalize()
print(f"11):{Dx}")
print(f"12):{Dx1}")
print(f"13):{Dx2}")
Cou = name.count("l")
Cou1 = name.count("l", 4)
print(f"14):{Cou}")
print(f"15):{Cou1}")
Fin = name.index("N")
Fin1 = name.find("N")
Fin2 = name.index("X le")
Fin3 = name.index("e")
print(f"16):{Fin}")
print(f"17):{Fin1}")
print(f"18):{Fin2}")
print(f"19):{name[:2:]}")
print(f"20):{name[0:3]}")
print(f"21):{name[-2:]}")
print(f"22):{Fin3}")
```

### 10、使⽤for循环对s="321"进⾏循环，打印的内容依次是："倒计时3秒"，"倒计时
2秒"，"倒计时1秒"，"出发！"。
```python
s = "321"
for sec in s:
    print(f"倒计时{sec}秒！")
print("出发！")
```


### 11、升级题：实现⼀个整数加法计算器（多个数相加）：
如：content = input("请输⼊内容:") ⽤户输⼊：5+9+6 +12+ 13，然后进⾏
分割再进⾏计算。
```pythoncontent = input("请输入内容：")
Sum = 0
Sp = content.split('+')
Su = Sp
for i in range(0, len(Sp)):
    Su[i] = int(Sp[i])
    # print(f"Sp:{Sp}")
    # print(f"Su:{Su}")
    Sum += Su[i]
print(f'输入数字和为：{Sum}')

```


### 12、计算⽤户输⼊的内容中有⼏个整数（以个位数为单位）。
如：content = input("请输⼊内容：") # 如fhdal234slfh98769fjdla
```python
Num = "121ddsjfksjfg12548"
Sm = "".join(list(filter(str.isdigit, Num)))
print(len(Sm))
```

### 13、(升级题)判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海
⾃来⽔来⾃海上(升级题)
```python
Str = input("请输入你要判断回文的话：")
i = 0
for kk in range(0, len(Str)):
    j = len(Str) - 1
    # print(len(Str))
    if Str[i] != Str[j]:
        print("不是回文")
        break
        # print(Str[i], Str[j])
        i += 1
        j -= 1
        # print(i, j)
    else:
        print("是回文")
```

### 14、制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名
字和爱好进⾏任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
```python
while 1:
    Name = input("请输入您用户名：")
    Site = input("请输您入地点是：")
    Hobby = input("请输入您的爱好：")
    print(f"敬爱可亲的{Name}，最喜欢在{Site}地方干{Hobby}")
    break
```

### 15、写代码，完成下列需求：
- ⽤户可持续输⼊（⽤while循环），⽤户使⽤的情况：
- 输⼊A，则显示⾛⼤路回家，然后在让⽤户进⼀步选择：
- 是选择公交⻋，还是步⾏？
- 选择公交⻋，显示10分钟到家，并退出整个程序。
- 选择步⾏，显示20分钟到家，并退出整个程序。
- 输⼊B，则显示⾛⼩路回家，并退出整个程序。
- 输⼊C，则显示绕道回家，然后在让⽤户进⼀步选择：
- 是选择游戏厅玩会，还是⽹吧？
- 选择游戏厅，则显示 ‘⼀个半⼩时到家，爸爸在家，拿棍等你。’并让其
- 重新输⼊A，B,C选项。
- 选择⽹吧，则显示‘两个⼩时到家，妈妈已做好了战⽃准备。’并让其重
- 新输⼊A，B,C选项。
```python
while 1:
    Ds = input("请输入你要回家的路径 A/B/C:")
    if Ds == 'A':
        Bw = int(input("请输入数字：1.公交 2.步行："))
        if Bw == 1:
            print("公交要10分钟到家")
            break
        else:
            print("步行要20分钟到家")
            break
    elif Ds == 'B':
        print("走小路回家")
        break
    else:
        print("绕道回家，那么你想？")
        Rd = input("你想干啥？：1.游戏厅玩会 2.网吧:")
        if Rd == 1:
            print("‘⼀个半⼩时到家，爸爸在家，拿棍等你,重新输入!")
        else:
            print("两个⼩时到家，妈妈已做好了战⽃准备，重新输入!")
```
