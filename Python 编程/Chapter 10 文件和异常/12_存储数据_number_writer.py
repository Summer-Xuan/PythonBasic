import json

numbers = [1,2,34,5,5]
"""
函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象。
"""
filename = 'demo\\numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)