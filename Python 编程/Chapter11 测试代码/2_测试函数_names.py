from name_function import get_formatted_name
import unittest

class NamesTestCase(unittest.TestCase):
    "测试name_function.py"
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样地姓名吗？"""
        formatted_time = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_time, "Janis Joplin")


    def test_first_last_middle
unittest.main()

