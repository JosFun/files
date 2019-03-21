import json

filename = "numbers.json"

with open(filename) as f_obj:
    numbers = json.load(f_obj)
f_obj.close()

print(numbers)