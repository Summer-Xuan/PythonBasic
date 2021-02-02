import unittest

class TestClass(unittest.TestCase):

    # 该方法会首先执行，相当于做测试前的准备工作
    def setUp(self):
        pass

    # 该方法会在测试代码执行完后执行，相当于做测试后的扫尾工作
    def tearDown(self):
        pass

    def test_app_exists(self):
        pass



