filename = 'programming.txt'
"""要让每个字符串都单独占一行，需要在write()语句中包含换行符"""

with open(filename, 'w') as file_object:
    file_object.write('I Love programming.\n')
    file_object.write('I Love creating new games.\n')
