import json

x = {
  "chaves": ["chaves do 8", "14/04/2017", "RECEP_01"],
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)
