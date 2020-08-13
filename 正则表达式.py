# re模块
import re
# re.match(pattern, string, flags=0) pattern 是指匹配的正则表达式；string 是指要匹配的字符串；flags 为标志位，用于控制正则表达式的匹配方式，如是否区分大小写、多行匹配等
# re.match() 只匹配字符串开始的字符 如果匹配成功，re.match()方法就返回一个匹配的对象，否则返回 None
print(re.match('hello', 'hello world').span())

# re.search() 匹配整个字符 扫描整个字符串，如果匹配成功，re.search()方法就返回一个匹配的对象，否则返回 None
print(re.search('hello', 'hello world').span())  # 在起始位置匹配 
print(re.search('world', 'hello world').span())  # 不在起始位置匹配 


# 贪婪模式 非贪婪模式



