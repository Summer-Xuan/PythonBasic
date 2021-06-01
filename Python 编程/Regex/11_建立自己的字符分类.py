# [] - ^
#
# 使用方括号建立自己的字符分类
import re
voweRegex = re.compile(r'[aeiouAEIOU.]') # 注意：方括号内，不需要加上倒斜杠转义.*?或(),如此时括号内的句点不需要加\
mo = voweRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

# 使用短横线表示字母或数字的范围。
# 字符分类[a-zA-Z0-9]将匹配所有小写字母、大写字母和数字


# 通过在字符分类的左方括号后加上一个插入符^,表示将匹配不在这个字符分类中的所有字符。
consonantRegex = re.compile(r'[^aeiouAEIOU.]')
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)