# 在正则表达式中，.(句点)字符成为‘通配符’。它匹配除了换行之外的所有字符。
# 句点只匹配一个字符。
import re
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
