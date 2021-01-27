"""
方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点
"""
filename = 'demo\\demo.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split('.')
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
