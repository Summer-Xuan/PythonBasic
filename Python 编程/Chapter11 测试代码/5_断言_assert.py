"""
断言就是判断1个函数或对象的1个方法所产生的结果是否符合你期望的那个结果。
"""

def num_div(num1, num2):
    """
    assert断言后面是一个表达式， 如果表示返回真，则断言成功，程序能够继续往下执行，
    如果表达式返回假，则断言失败，assert会抛出异常AssertionError,终止程序继续往下执行
    """
    try:
        assert isinstance(num1, int)
        assert isinstance(num2, int)
        assert num2 != 0

    except Exception as e: # except捕捉不到assert的错误？
        print("Error Message:{}".format(e))

    else:
        print(num1/num2)

if __name__ == '__main__':
    num_div(100, 10)
