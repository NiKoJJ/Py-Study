import random
words=['Hello','Python','different','answer','continue','code','game','windows']
iscon='Y'
# word = random.choice(words)
# l=len(word)
# corret=word
# luanxu=""
# position = random.randrange(0,l,1)
# str_a=str(word[position])
# print(word)
# print(position)
# print(word[position])
# print(str_a)
# luanxu+=str_a
# print(luanxu)


while iscon=='Y' :
    word = random.choice(words)
    l=len(word)
    corret=word
    luanxu=""
    while len(luanxu)<len(word):
        position = random.randrange(0,l,1)
        str_a=str(word[position])    # IndexError: string index out of range
        luanxu += str_a
        word = word[:position] + word[(position + 1):]
    print('乱序后单词：', luanxu)

    guess=input('\n请你猜：')
    while guess!= corret and guess!="":
        print('对不起，不正确！')
        guess=input('继续猜：')
        if guess==corret:
            print('恭喜你，猜对了！')
        iscon=input('\n是否继续(Y/N)：')
