import json

test='{"user_id":"hola"}'

objtest=json.loads(test)

print(objtest)

print(objtest.get('pepe'))