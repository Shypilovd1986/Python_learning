import json
from random import randint

# JSON  -JavaScript Object Notation, A common use of JSON is to read data from a web server, and display the data in a
# web page. Применяется в веб-приложениях как для обмена данными между браузером и сервером (AJAX), так и между
# серверами (программные HTTP-сопряжения).
# !!!!!!!  use only double quotes not single
str_json ="""
{
    "response":{
        "count":5832844,
        "items":[{
            "first_name":"Dmitriy",
            "id":12534321,
            "age":37   
        },{
            "first_name":"Mary",
            "id":22534321,
            "age":30
        }]
    }
}
"""

print(type(str_json))
data = json.loads(str_json)
print(type(data))
for item in data['response']['items']:
    item['likes'] = randint(100, 200)
    item['value'] = None
for item in data['response']['items']:
    print(item['first_name'], item['age'], item['likes'])
print(data)

new_json = json.dumps(data, indent=2)
print(type(new_json))
print(new_json)

# with open('my.json', 'w') as file:
#     json.dump(new_json, file, indent=2)
with open('my.json', 'r') as file:
    data1 = json.load(file)
print(data1)
print(type(data1))
# !!!!  decoding JSON -> Python
# object -> dict
# array ->list
# string -> str
# number(int) -> int
# number(real) -> float
# true -> True
# false -> False
# null -> None
