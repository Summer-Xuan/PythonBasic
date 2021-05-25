# Python的正则表达式默认是‘贪心’的，这表示在有二义的情况下，会尽可能匹配最长的字符串。
# 花括号的‘非贪心’版本匹配尽可能最短的字符串，即在结束的花括号后跟着一个问号。
"""
注意：
问号在正则表达式中可能有两种含义：
声明非贪心匹配；
表示可选的分组 0或1次匹配
"""


# 贪心
import re
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

# 非贪心
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())