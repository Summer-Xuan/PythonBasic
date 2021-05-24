# 字符？表明它前面的分组在这个模式中是可选的,即匹配问好之前的分组零次或一次。0次或1次

# 例1
import re
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# 例2
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())
print(mo2.group(1)) # ()?返回None