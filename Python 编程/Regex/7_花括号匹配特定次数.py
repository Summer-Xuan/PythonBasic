# 如果想要一个分组重复特定次数，就在正则表达式中该分组的后面，跟上花括号包围的数字
# 除了一个数字，可以指定一个范围｛3，5｝
# 可以不写花括号中的第一个或第二个数字，不限定最小值或最大值。(Ha){3,}将匹配3次或更多次，(Ha){,5}将匹配0到5次实例。

import re
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 == None)

