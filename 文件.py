# open()函数 open(file_name [, access_mode][, buffering]) 
# access_mode 参数是指打开文件的模式，对应有只读、写入、追加等。access_mode 参数不是必需的（不带 access_mode 参数时，要求 file_name 存在，否则报异常），默认的文件访问模式为只读（r）
# mode参数： r-只读方式打开  rb-二进制格式打开只读  r+ --读写   rb+ --二进制格式打开 读写
#           w-只写入  wb-二进制只写
#           w+    wb+
#  文件指针放在文件结尾   a   ab   a+   ab+
# buffering 用于控制文件的缓存
path1 = 'F:/test.txt'
f_name = open(path1)
print(f_name.name)

# 区分 绝对路径 相对路径
# 文件读写
path1 = './second.txt'  # (..)表示父文件夹  （.)当前文件夹
f_na = open(path1, 'w')
f_na.write('Hello,Python!')
f_na = open(path1, 'a+')
st = ' 文件尾部'
print(f'length:{f_na.write(st)}')
f_na = open(path1, 'r')
print(f'read result:{f_na.read()}')
f_na.close()

print('--------------------行的读写---------------------')

path2 = './file_readline.txt'
finame = open(path2, 'w')
finame.write('Hello World!\n')
filename = open(path2, 'a')
finame.write('Welcome')
finame = open(path2, 'r')
# print(f'按行读取：{finame.readline()}')
print(f'多行读取：{finame.readlines()}')  # 此时输出的字符串列表

str_list = ['Hello World!\n', 'Welcome!\n', 'welcome\n']
list_name = open(path2, 'a')
list_name.writelines(str_list)
list_name = open(path2, 'r')
print(f'读取列表结果：{list_name.readlines()}')

# 引入 with 语句自动调用 close()方法,将上面改写
'''
with open(path2,'w') as finame:
    finame.write('Hello World!\n')
with open(path2,'a') as finame:
    finame.write('Welcome')
with open(path2,'r') as finame:
    print(f'多行读取：{finame.readlines()}')
'''


# 文件内容的迭代
l = './diedai.txt'
with open(l, 'w') as f:
    f.write('Hello!\n')
f = open(l)
while True:
    f_str = f.read(1)
    if not f_str:
        break
    print(f'read str is :{f_str}')

# 按行迭代读取
with open(l,'a') as le:
    le.write('1、With my own ears I clearly heard the heart beat of the nuclear bomb\n'
             '我亲耳清楚地听到原子弹的心脏的跳动\n'
             '2、The bold folk fold up the gold and hold it in hand\n'
             '大胆的人们将黄金折叠起来拿在手里\n')
le = open(l)
while True:
    line =le.readlines(1)
    if not line:
        break
    print(f'按行读取结果：{line}')
le.close()
