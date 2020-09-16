import random
# random.random()生成一个 随机小数
r=random.random()
print(r)

# random.uniform(a,b) 生成一个指定范围的随机小数
ru=random.uniform(10,30)
print(ru)

# randon.randint(a,b) 生成指定范围的随机整数
rr=random.randint(3,50)
print(rr)

# random.randrange(start，stop,step)
rrd=random.randrange(10,60,3)
print(rrd)

# random.choice() 从序列中获取一个随机元素
A='Study Python'
B=['Study','Python']
C=('study','Python','study python')
print(random.choice(A))
print(random.choice(B))
print(random.choice(C))

# random.sguffle(x[,random]) 将一个列表中元素打乱
d=["Python","is","easy","so on"]
rs=random.shuffle(d)
print(rs)




# import random
# words=['Hello','Python','different','answer','continue','code','game','windows']
# iscon='Y'
# # word = random.choice(words)
# # l=len(word)
# # corret=word
# # luanxu=""
# # position = random.randrange(0,l,1)
# # str_a=str(word[position])
# # print(word)
# # print(position)
# # print(word[position])
# # print(str_a)
# # luanxu+=str_a
# # print(luanxu)
#
#
# while iscon=='Y' :
#     word = random.choice(words)
#     l=len(word)
#     corret=word
#     luanxu=""
#     while len(luanxu)<len(word):
#         position = random.randrange(0,l,1)
#         str_a=str(word[position])    # IndexError: string index out of range
#         luanxu += str_a
#         word = word[:position] + word[(position + 1):]
#     print('乱序后单词：', luanxu)
#
#     guess=input('\n请你猜：')
#     while guess!= corret and guess!="":
#         print('对不起，不正确！')
#         guess=input('继续猜：')
#         if guess==corret:
#             print('恭喜你，猜对了！')
#         iscon=input('\n是否继续(Y/N)：')
