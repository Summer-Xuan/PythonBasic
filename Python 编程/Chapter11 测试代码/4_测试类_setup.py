# -*- coding: utf-8 -*-
import unittest
from suvery import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        unittest.TestCase类包含方法setUp()，只需创建这些对象一次，并在每个测试方法中使用它们。
        如果在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法。
        """
        question = "What language did you first learn to speak?"
        # 方法setUp()做了两件事：创建一个调查对象；创建一个答案列表。
        # 两样东西的变量名包含前缀self（即存储在属性中），因此可在这个类的任何地方使用。
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

        def test_store_single_response(self):
            """测试单个答案会被妥善地存储"""
            self.my_survey.store_response(self.reponses[0])
            self.assertIn(self.reponses[0], self.my_survey.responses)

        def test_store_three_responses(self):
            for response in self.responses:
                self.my_survey.store_response(response)
            for response in self.responses:
                self.assertIn(response, self.my_survey.responses)



unittest.main()

