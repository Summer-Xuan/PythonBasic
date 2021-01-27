import json

filename = 'demo\\numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)