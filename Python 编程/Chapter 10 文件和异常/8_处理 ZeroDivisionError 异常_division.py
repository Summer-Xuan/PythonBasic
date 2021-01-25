
"""
如果try代码块中的代码运行起来没有问题，Python将跳过except代码块；
如果try代码块中的代码导致了错误，Python将查找这样的except代码块，并运行其中的代码，即其中指定的错误与引发的错误相同。
如果try-except代码块后面还有其他代码，程序将接着运行，因为已经告诉了Python如何处理这种错误。
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")