import json

# 1.读取json
with open("../file/dabao.json", 'r') as f:
    content = f.read() # open来读取文件
    a = json.loads(content) # json.loads()将读取json内容转化为python字典
    print(type(a))
    print(a)

# 2.将字典保存为json
a = {
    "name": "dabao",
    "id":123,
    "hobby": {
        "sport": "basketball",
        "book": "python study"
    }
}
# 首先通过json.dumps()把dict转为为json字符串;若防止中文被转义：加参数,ensure_ascii=False,默认为True.
b = json.dumps(a)
# print(b)
print(type(b))
with open('../file/new_json.json','w') as f2:
    f2.write(b) # 再将字符串写入json文件中


