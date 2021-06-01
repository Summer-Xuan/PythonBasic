# Regex对象有search方法和findall方法
"""
search()将返回一个Match对象，包含被查找字符串中的“第一次”匹配的文本；
findall()方法将返回一组字符串，包含被查找字符串中的所有匹配,返回字符串列表。
"""
# search()
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell:415-555-9999 Work:212-555-0000')
print(mo.group())

# findall()
mo2=phoneNumRegex.findall('Cell:415-555-9999 Work:212-555-0000')
print(mo2)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo3 = phoneNumRegex.findall('Cell:415-555-9999 Work:212-555-0000')
print(mo3)

mo4 = phoneNumRegex.search('Cell:415-555-9999 Work:212-555-0000')
print(mo4.group(1)) # 被查找字符串中的“第一次”匹配的文本

