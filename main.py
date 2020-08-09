numa = 10
if numa > 10:
    print('numa value >10')
elif 0 <= numa <= 10:
        print('numa value 0-10')
else:
        print('numa value <0')


print('‐‐‐‐‐for循环字符串‐‐‐‐‐‐‐‐‐‐‐')
for ler in 'good':      #for循环字符串
    print(f'当前字母 :{ler}')

print('------迭代工具--------------')
student=['小明', '小杰', '小张']
number=[830, 831, 832]
for i in range(len(student)):
    print(f'{student[i]}的学号是：{number[i]}')

print('----------------------------')
name = 'xiaojie'
if name == 'xiaojie':
    print(f'hello,{name}')
elif name == 'xiaoming':
    pass
else:
    print('nothing')


import random
num=random.randint(0, 100)
print(num)

print('*****************************')
print('\n')
import sys
import random
number = random.randint(1,100)
guess=0
while 1:
    num_input = input('请猜一个1-100的数，退出游戏请输入q：')
    if number == int(num_input):
        guess += 1
        print(f'恭喜猜对了！正确数字是：{num_input},共计猜测{guess}次')
        exit(0)
    elif number > int(num_input):
        guess += 1
        print(f'你猜的数字偏小，目前已经猜测{guess}次')
    elif number < int(num_input):
        guess += 1
        print(f'你猜测的数字偏大，目前已经猜测{guess}次')
    else:
        print('出现错误，联系工作人员进行处理')
