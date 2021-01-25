with open("pi_digits.txt") as file_object:
    """ 
    1.open()返回一个文件对象；
    2.方法read()读取这个文件的全部内容，并将其作为一个长长的字符串存储在变量contents中；
    3.read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行；
    4.Python方法rstrip()删除（剥除）字符串末尾的空白；
    """
    contents = file_object.read()
    print(contents.rstrip())