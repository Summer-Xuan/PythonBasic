filename = 'programming.txt'
"""
1.如果省略了模式实参，Python将以默认的只读模式打开文件.
2.如果要写入的文件不存在，函数open()将自动创建它.
3.以写入（'w'）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件.
4.Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。
"""
with open(filename, 'w') as file_object:
    file_object.write("I love programming")
