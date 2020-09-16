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

print('**------------------------------------**')


# 继承
class Animal(object):  # 类Animal
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f'Animal: {self.name} is running .......')

    def __run01(self):  # 属于类Animal的私有方法，外部不可调用
        print(f'Looking these {self.name} is running .......,Do you want try this? hahaha')

    def run02(self):
        print(f'Looking these {self.name} is running .......,Do you want try this? hahaha')


class Dog(Animal):  # 类Dog
    pass


class Cat(Animal):  # 类Cat
    def __init__(self, name, food):
        self.food = food
        self.name = name

    def eat(self):  # 定义自己的类方法
        print(f'{self.name} eat {self.food}')


# Dog()作为Animal子类可以调用父类中方法
dog = Dog('dog')
dog.run()

# 类Cat中进行了一次__init__定义，那么作为Animal的子类进行实例初始化时调用的是子类本身的__init__()
# 同时在子类中定义了一个属于自己的类方法eat()，定义的实例可以调用自己的类方法
cat = Cat('cat', 'fish')
cat.run()
cat.eat()

# 父类私有方法不可以调用
animal = Animal('Birds')
animal.run()
animal.run02()

print('----------------------------------------')


# 多重继承
# 问题：多重继承时是在定义类时在类括号中添加多个父类，那么以上面的Animal（），Dog(),Cat()类为例,
# 后面两个是Animal的子类，在构建多重继承类时是否可以将这个三个作为新类的三个父类呢？

# ('------------哺乳类与鸟类--------------')
# 哺乳类
class Mammal(object):
    def M(self):
        print('Mammal')


# 鸟类
class Brid(object):
    def B(self):
        print('Bird')


# ('-----------功能：run fly-------------------')
# run
class Run(object):
    def run(self):
        print('running...')


# fly
class Fly(object):
    def fly(self):
        print('Flying...')


# ’---------------------------------------------‘

class Dog(Mammal, Run):
    pass


class Brids(Brid, Fly):
    pass


dog = Dog()
a = dog.M()
b = dog.run()
Brid = Brids()

# 多态，多态会根据对象（或类）的不同而表现出不同的行为
# 当子类和父类存在相同的 run()方法时，子类的 run()方法会覆盖父类的 run()方法，在代码运行时总是会调用子类的 run()方法，这种调用方式称为多态


print(f'{isinstance(dog, Dog)}')  # 判断继承关系

print(dir('abc'))  # dir() 获取一个对象的所有属性和方法

print('--------------******-------------------')

# __iter__()方法返回一个迭代对象，Python 的 for 循环会不断调用该迭代对象的__next__()方法，从而获得循环的下一个值，直到遇到 StopIteration 错误时，退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:  # 退出循环条件
            raise StopIteration
        return self.a


for n in Fib():
    print(n)

# __getitem__ 获取元素
class Fib1(object):
    def __getitem__(self, item):
        a,b=1,1
        for x in range(item):
            a,b = b,a+b
        return a

fib=Fib1()
print(f'第四个元素fib[3]:{fib[3]}')


# __getattr__()方法动态返回一个属性
print('---------------------------------------------------')
class item(object):
    def __init__(self):
        self.name='xiaoming'

    def __getattr__(self, item):
        if item == 'score':
            return 95
re=item()
print(f'name:{re.name}')
print(f'动态属性：{re.score}')


# __call__() 方法 直接在实例内部调用实例
# 对实例进行直接调用就像对一个函数进行调用一样，完全可以把对象看成函数，把函数看成对象，因为这两者本来就没有根本区别

print('--------------------------------------------------------')
class new(object):
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print(f'名称：{self.name}')

sy=new('Jack')
sy()


# /////////////////////////////////////////////////////////////////////

class Student(object):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f'学生信息：{self.name} {self.grade}'


print('***-----------------------****--------------------***')
print(Student('小明', 98))
