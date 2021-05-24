# 管道|符匹配多个表达式中的一个且匹配第一次出现的匹配文本将作为Match对象返回。
import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())


mo2 = heroRegex.search('Tina Fey and Battman')
print(mo2.group())

# 匹配多个模式中的一个
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))