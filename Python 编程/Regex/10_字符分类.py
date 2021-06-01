"""
\d  0到9的任何数字
\D  除0到9的数字以外的任何字符
\w  任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
\W  除字母、数字和下划线以外的任何字符
\s  空格、制表符或换行符（可以认为是匹配“空白”字符）
\S  除空格、制表符和换行符以外的任何字符
"""
import re
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers,11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)
