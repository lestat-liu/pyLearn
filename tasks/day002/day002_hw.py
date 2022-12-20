# -*- coding:utf-8 -*-
"""
@author: 'xcld'
@file: day002_hw.py
@time: 2022-12-07 12:01
"""
# Num = int(input("请输入一个要猜测的数字："))
# Sum = 1
# while Sum > 0:
#     if Num > 66:
#         print('猜测的结果:{} 大了!'.format(Num))
#     elif Num < 66:
#         print('猜测的结果:{} 小了!'.format(Num))
#     else:
#         print('猜测结果是:{} 正确！'.format(Num))
#     Sum -= 1


# Sum = 3
# # i = 1
# # while i > 0:
# while Sum > 0:
#     Num = int(input("请输入一个要猜测的数字："))
#     if Num > 66:
#         print('猜测的结果:{} 大了!'.format(Num))
#     elif Num < 66:
#         print('猜测的结果:{} 小了!'.format(Num))
#     elif Num == 66:
#         print('猜测结果是:{} 正确！'.format(Num))
#         break
#     Sum -= 1
# else:
#         print("太笨了你！其实，我对你是有一些失望的。当初给你定级p7，是高于你面试时的水平的。\n我是希望进来后，你能够拼一把，快速成长起来的。p7这个层级，不是把事情做好就可以的。\n你需要有体系化思考的能力。你做的事情，他的价值点在哪里？你是否作出了壁垒，形成了核心竞争力？\n你做的事情，和公司内其他团队的差异化在哪里？你的事情，是否沉淀了一套可复用的物理资料和方法论？\n为什么是你来做，其他人不能做吗？你需要有自己的判断力，而不是我说什么你就做什么。\n后续，把你的思考沉淀到日报周报月报里，我希望看到你的思考，而不仅仅是进度。\n另外，提醒一下，你的产出，和同层级比，是有些单薄的，马上要到年底了，加把劲儿。\n你看咱们团队的那个A, 人家去年晋升之前，可以一整年都在项目室打地铺的。\n成长，一定是伴随着痛苦的，当你最痛苦的时候其实才是你成长最快的时候。加油")

# i = 'true'
# while i:
#     Prime = int(input("请输入你要判断的数："))
#     Bu = Prime > 1 and Prime % Prime == 0 and Prime // Prime == 1
#     if Bu:
#         print(f"{Prime}是一个质数")
#         break
#     else:
#         print(f"{Prime}不是质数")
#         break

# for x in range(101):
#     if (x == 2) or (x == 3):
#         print(f'质数是{x}')
#     else:
#         count = 0
#         j = 2
#         while j <= (x - 1):
#             flag = x % j
#             if flag != 0:
#                 count += 1
#                 j += 1
#                 break
#             else:
#                 if count == (x - 2):
#                     print(f'这是质数{x}')
#                     break

# Prime = int(input("请输入一个正整数："))
# if Prime == 2 and Prime > 1:
#     print(f'{Prime}是质数')
# elif Prime == 3:
#     print(f'{Prime}是质数')
# else:
#     count = 0
#     count1 = 0
#     i = 2
#     for j in range(i, Prime):
#         if Prime % j == 0:
#             count += 1
#             if count is not 0:
#                 print(f'{Prime}不是质数', j)
#                 print("count:", count)
#                 # break
#         else:
#             count1 += 1
#             if count1:
#                 print("count1:", count1)
#                 print(f'{Prime}是质数')
#                 # break
# count = 0
# count1 = 0
# for k in range(2, 10):
#     for j in range(2, 9):
#         if k % j == 0:
#             print(f"k:{k} j:{j}")
#             count += 1
#             print("count:", count)
#         else:
#             count1 += 1
#             print("count1:", count1)
#             print(f"k:{k} j:{j}")

# from math import sqrt
# n = int(input("请输入一个正整数："))
# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             print(f"{n}这不是质数")
#             # return False
#         else:
#             print(f"{n}是质数")
#     # return True

# 7、

# Adv = input("请输入你认为牛逼的广告语：")
# if Adv.count("最") or Adv.count("第一") or Adv.count("稀缺") or Adv.count("国家级"):
#     print("广告语不合法！", Adv)
# else:
#     print("广告语很棒!", Adv)


# # 批改：
# st = "heeeddd"
# print(st.count("e"))   #  这里要统计e出现的次数，用在这里不合理，会降低效率
#
# # 应该用in,只要出现一次就行;或者index只要出现一次就行
# print("e" in st)
# print(st.index("e"))



# Sum = 3
# Scr = "Ak123"
# while Sum:
#     Ipu = input("请输入密码：")
#     if Ipu == Scr:
#         print("密码输入正确!")
#         break
#     else:
#         Sum -= 1
#         print(f"请重新输入，还剩{Sum}次机会！")


# name = " aleX leNb "
# print(name)
# Rlsp = name.strip()
# print(f"1):{Rlsp}")
# print(f"2):{name[2:]}")
# print(f"3):{name[:-3]}")
# # print(f"4):{name[2:9]}")
# Yc = Rlsp.strip('ab')
# print(f"4):{Yc}")
# Kt = name.startswith("al")
# print(f"5):{Kt}")
# Jw = name.endswith("Nb")
# print(f"6):{Jw}")
# Rep = name.replace("l", "p")
# Rep1 = name.replace("l", "p", 1)
# print(f"7):{Rep}")
# print(f"8):{Rep1}")
# Spl = name.split("l")
# Spl1 = name.split("l", 1)
# print(f"9):{Spl}")
# print(f"10):{Spl1}")
# Dx = name.upper()
# Dx1 = name.lower()
# Dx2 = name.title()
# print(f"11):{Dx}")
# print(f"12):{Dx1}")
# print(f"13):{Dx2}")
# Cou = name.count("l")
# Cou1 = name.count("l", 4)
# print(f"14):{Cou}")
# print(f"15):{Cou1}")
# Fin = name.index("N")
# Fin1 = name.find("N")
# Fin2 = name.index("X le")
# Fin3 = name.index("e")
# print(f"16):{Fin}")
# print(f"17):{Fin1}")
# print(f"18):{Fin2}")
# print(f"19):{name[:2:]}")
# print(f"20):{name[0:3]}")
# print(f"21):{name[-2:]}")
# print(f"22):{Fin3}")

# s = "321"
# for sec in s:
#     print(f"倒计时{sec}秒！")
# print("出发！")

# content = input("请输入内容：")
# Sum = 0
# Sp = content.split('+')
# Su = Sp
# for i in range(0, len(Sp)):
#     Su[i] = int(Sp[i])
#     # print(f"Sp:{Sp}")
#     # print(f"Su:{Su}")
#     Sum += Su[i]
# print(f'输入数字和为：{Sum}')

# Num = "121ddsjfksjfg12548"
# Sm = "".join(list(filter(str.isdigit, Num)))
# print(len(Sm))


# 13
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



# while 1:
#     Name = input("请输入您用户名：")
#     Site = input("请输您入地点是：")
#     Hobby = input("请输入您的爱好：")
#     print(f"敬爱可亲的{Name}，最喜欢在{Site}地方干{Hobby}")
#     break
# while 1:
#     Ds = input("请输入你要回家的路径 A/B/C:")
#     if Ds == 'A':
#         Bw = int(input("请输入数字：1.公交 2.步行："))
#         if Bw == 1:
#             print("公交要10分钟到家")
#             break
#         else:
#             print("步行要20分钟到家")
#             break
#     elif Ds == 'B':
#         print("走小路回家")
#         break
#     else:
#         print("绕道回家，那么你想？")
#         Rd = input("你想干啥？：1.游戏厅玩会 2.网吧:")
#         if Rd == 1:
#             print("‘⼀个半⼩时到家，爸爸在家，拿棍等你,重新输入!")
#         else:
#             print("两个⼩时到家，妈妈已做好了战⽃准备，重新输入!")
# ii = 6 or 2 > 1
# if ii:
#     print("true")
# else:
#     print("false")


