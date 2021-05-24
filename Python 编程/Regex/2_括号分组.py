# 1.利用括号分组
"""
1.添加括号将在正则表达式中创建‘分组’
2.向group()匹配对象传入整数1或2，就可以取得匹配文本的不同部分。
3.向group()方法传入0或不传入参数，将返回整个匹配的文本。
"""
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

print('*'*50)
"""
使用倒斜杠对括号进行字符转义
"""
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242')
print(mo.group(1))