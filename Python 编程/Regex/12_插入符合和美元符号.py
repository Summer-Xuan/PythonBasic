# 插入符号^表明匹配必须发生在被查找文本开始处
import re
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello World')
print(mo)


# 美元符号$表示该字符串必须以这个正则表达式的模式结束。
# 正则表达式r'\d$'匹配以数字0到9结束的字符串
endsWithNumber = re.compile(r'\d$')
mo1 = endsWithNumber.search('Your number is 42')
print(mo1)
print(endsWithNumber.search('Your number is forty two') ==None)


# 同时使用^和$，表明整个字符串必须匹配该模式，也就是说，只匹配该字符串的某个自己是不够的
# 正则表达式r'\d+$'匹配以数字0到9结束的字符串。
whoStringIsNum = re.compile(r'^\d+$')
print(whoStringIsNum.search('1234567890'))
print(whoStringIsNum.search('1234567zy098')==None)
print(whoStringIsNum.search('123 4567zy098')==None)





