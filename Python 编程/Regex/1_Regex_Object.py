import re
"""
1.用import re导入正则表达式模式。
2.用re.compile()函数创建一个Regex对象(记得使用原始字符串)
3.向Regex对象的search()方法传入想查找的字符串。它返回一个Match对象。
4.调用Match对象的group方法，返回实际匹配文本的字符串。
"""
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # 期待的模式传给re.compile(),得到regex对象
mo = phoneNumRegex.search('My number is 415-555-4242') # Regex对象的search()方法查找传入的字符串，如果找到该模式，search()方法将返回一个Match对象
print('Phone number found:'+ mo.group()) # Match对象有一个group()方法，它返回被查找字符串中实际匹配的文本。

