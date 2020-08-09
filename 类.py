class MyClass(object):
    i = 123

    def __init__(self, name):  # 初始化
        self.name = name

    def f(self):
        return 'hello,' + self.name


use_class = MyClass('小杰')
print(f'调用类属性：{use_class.i}')
print(f'调用类的方法：{use_class.f()}')

print('*-------------------------------------------*')


class DefaultInit(object):
    def __init__(self):
        print('我是不带参数的__init__方法')

    def __init__(self, p):
        print(f'我是一个带参数的__init__方法，参数值为：{p}')


DefaultInit('Hello')
print('类实例化结束')

print('*-------------------------------------------*')


# 第一参数永远是类的本身实例变量self
class Student(object):
    def __init__(self, name, score):
        self.__name = name  # 私有变量
        self.__score = score

    def info(self):
        print(f'学生：{self.__name};分数：{self.__score}')

    def get_name(self):  # 从外部获取
        return self.__name

    def get_score(self):
        return self.__score

    def setting_score(self, score):  # 修改
        if 0 <= score <= 100:
            self.__score = score
        else:
            return self.__score

    def setting_name(self, name):
        self.__name = name
        return self.__name


stu = Student('NikoJJ', 98)
stu.info()
print(f'{stu.get_name()}')
a = stu.setting_name('Jack')
print(f'{a}')
