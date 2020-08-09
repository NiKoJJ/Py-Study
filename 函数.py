def hello():
    print('Hello,World!')


hello()

new = abs
print(f'{new(-3.14)}')
print(f'{new(-5)}')


def sum_n():
    a = 10
    b = 20
    print(a + b)
    print(f'{a + b}')


sum_n()


def person_info(age, name):
    print(f'年龄：{age}')
    print(f'姓名：{name}')


print('****************************')
person_info('21岁', '小杰')
print('\n')
person_info('小杰', '21岁')
print('----------------------------')
person_info(name='小明', age='18岁')


def person_info_var(age, *vartuple):
    print(age)
    for var in vartuple:
        print(f'我属于不定长参数部分：{var}')
    return


print('---------不带可变参数-----------')
person_info_var('小杰，20岁啦!')
print('------------------------------')

print('\n')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
other = {'城市': '北京', '爱好': '编程', '学校': '西南交通大学'}


def per_info(name, number, **key):
    print(f'姓名：{name},学号：{number}，其他：{key}')


per_info('小明', '2018114789', **other)

# 必需参数、默认参数(age=20)、可变参数（*key)、关键字参数

print('----------******-------------')


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(f'递归函数调用结果为：{fact(5)}')


def fact_n(num, res):
    if num == 1:
        return res
    else:
        return fact_n(num - 1, num * res)


import sys

sys.setrecursionlimit(10000)  # 深度设置为一万
print(fact_n(20, 1))

c = lambda x, y: x + y  # 匿名函数
print(f'匿名函数：{c(2, 3)}')
print('列表中大于3的元素有：', [item for item in filter(lambda x: x > 3, [1, 2, 3, 4, 5, 7])])

# 偏函数 将所要承载的函数作为 partial()函数的第一个参数，原函数的各个参数依次作为partial()函数的后续参数，除非使用关键字参数。
from functools import partial
from math import *

print(pi)


def mod(n, m):
    return n % m


mod_by_100 = partial(mod, 100)
print(f'{mod_by_100(7)}')

print('---------------------------------')
# 选择排序（升序、降序）
A = [-8, -9, 5, 6, 2, 3, 7]

print('升序：')


def sort1():
    for i in range(len(A)):
        minA = i  # 序号
        for j in range(i + 1, len(A)):
            if A[minA] > A[j]:
                minA = j
        A[i], A[minA] = A[minA], A[i]  # 交换位置
    return A


print(f'排序后：{sort1()}')

print('降序:')


def sort2(A):
    for i in range(len(A)):
        max_A = i  # 序号
        for j in range(i + 1, len(A)):
            if A[max_A] < A[j]:
                max_A = j
        A[i], A[max_A] = A[max_A], A[i]  # 交换位置
    return A


B = [-8, 9, 6, 2, 1, 4, -10]
print(f'排序后：{sort2(B)}')

print('---------升降合并-------------')


# 将升序和降序合并为一个程序
def get_sort(arr, order):
    for i in range(len(A)):
        p = i
        for j in range(i + 1, len(A)):
            if (arr[p] > arr[j]) and (int(order) > 0) or (arr[p] < arr[j]) and (int(order) < 0):
                p = j
        arr[i], arr[p] = arr[p], arr[i]
    return arr


print(get_sort(A, 1))
print(get_sort(A, -1))
