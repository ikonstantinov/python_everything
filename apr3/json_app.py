import json, os

obj = {1: (1, 2, 3), 'a': [2, 3, 4], True: None}

print("Hello")
f = json.dumps(obj)
print(f)
#d = json.loads(obj)
#print(d)

os.path.exists()