import time


# time()函数用于返回当前时间的时间戳 浮点数
# 当前时间戳
print(time.time())


# 时间间隔为：1.5 minutes
start_time = time.time()
time_add = start_time + 90
cha = time_add - start_time

print(f'时间间隔为：{cha / 60} minutes')


# strftime()接收时间元组，并返回以可读字符串表示的当地时间
# gmtime()函数用于讲一个时间戳转换为UTC市区的struct time，可选参数表示从1970.01.01.00.00.00到现在的秒数
# mktime(t)函数,t 是指结构化的时间或完整的 9 位元组元素,mktime()函数用于执行与 gmtime()、localtime()相反的操作，接收 struct_time 对象作为参数，返回用秒数表示时间的浮点数
# Aug 11 2020 14:08:37
t = (2020, 8, 11, 22, 8, 37, 1, 224, 0)
print(f'time.mktime()函数：{time.mktime(t)}')
t = time.mktime(t)
print(time.strftime('%b %d %Y %H:%M:%S', time.gmtime(t)))


# localtime([secs)作用是格式化时间戳为本地时间,如果 secs 参数未传入，就以当前时间为转换标准。该函数返回 time.struct_time 类型的对象 time.struct_time(
# tm_year=2020, tm_mon=8, tm_mday=11, tm_hour=22, tm_min=18, tm_sec=16, tm_wday=1, tm_yday=224, tm_isdst=0)
print(f'time.localtime()函数，参数为当前时间：\n{time.localtime()}')


# sleep(secs)函数,secs是指推行执行的秒数,用于时间延迟
print(f'开始：{time.ctime()}')
time.sleep(1)  # 等待1秒程序运行结束
print(f'结束：{time.ctime()}')


# asctime()函数 接收时间元组并返回一个可读的形式
t=time.localtime()
print(f'time.lacaltime()函数：{time.asctime(t)}')

# ctime()函数 把时间戳参数(默认为time.time())转换为time.asctime()形式
t0=1497154917.0
t=time.time()
print(f'ctime()函数：{time.ctime(t)}')
print(f'ctime()函数：{time.ctime(t0)}')


# clock()函数 在 Windows 系统中，第一次调用返回的是进程运行的实际时间，第二次之后的调用返回的是自第一次调用后到现在的运行时间。

# datatime模块，五个类 data（日期） time（时间） datetime（日期时间） timedelta(时间间隔） tzinfo(时区信息）
import datetime

t2=datetime.datetime.now()  # now()方法
print(f'现在时间datatime：{t2}')

t3=datetime.datetime.today()  # today()方法
print(f'today time: {t3}')

# strptime(data_string,format)
dt=datetime.datetime.now()
strp_dt=str(dt)
new_dt=datetime.datetime.strptime(strp_dt,'%Y-%m-%d %H:%M:%S.%f')  # 字符化，输出格式化
print(f'strptime()函数：{new_dt}   格式类型：{type(strp_dt)}')


# strftime()将datatime对象转换成格式字符串
strf_dt=dt.strftime('%Y-%m-%d %H:%M:%S')
print(f'strftime()函数：{strf_dt}   格式类型：{type(strf_dt)}')
t4=dt.strftime('%Y-%m-%d  %I:%M:%S %p')
print(f'年月日时分秒(%Y‐%m‐%d %H:%M:%S %p): {t4}')


# fromtimestamp()函数 根据时间戳创建一个datetime对象并返回
t5=datetime.datetime.fromtimestamp(time.time())
print(f'根据时间戳创建datetime对象：{t5}')

# calendar板块
import calendar

cal=calendar.calendar(2020,2,1,6)  # 年历 三个月一行 w:每日宽度 l:每星期的行数 c:间隔距离 每行长度：21*w+18+2*c
print(f'{cal}')
cal_21=calendar.calendar(2021,3,2,6)
print(f'2021年年历：\n{cal_21}')

cal_3=calendar.month(2020,8,2,1)
print(f'2020年8月：{cal_3}')

