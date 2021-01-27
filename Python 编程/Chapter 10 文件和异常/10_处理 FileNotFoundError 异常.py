"""使用文件时，一种常见的问题是找不到文件：
你要查找的文件可能在其他地方、文件名可能不正确或者这个文件根本就不存在。
对于所有这些情形，都可使用try-except代码块以直观的方式进行处理
 """

filename = 'alice.txt'

try:
    with open(filename) as file_object:
            contents = file_object.read()
except:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)


