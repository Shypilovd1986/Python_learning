import json

# from random import randint

# JSON  -JavaScript Object Notation, A common use of JSON is to read data from a web server, and display the data in a
# web page. Применяется в веб-приложениях как для обмена данными между браузером и сервером (AJAX), так и между
# серверами (программные HTTP-сопряжения).
# !!!!!!!  use only double quotes not single
# str_json ="""
# # {
# #     "response":{
# #         "count":5832844,
# #         "items":[{
# #             "first_name":"Dmitriy",
# #             "id":12534321,
# #             "age":37
# #         },{
# #             "first_name":"Mary",
# #             "id":22534321,
# #             "age":30
# #         }]
# #     }
# # }
# # """

# print(type(str_json))
# data = json.loads(str_json)
# print(type(data))
# for item in data['response']['items']:
#     item['likes'] = randint(100, 200)
#     item['value'] = None
# for item in data['response']['items']:
#     print(item['first_name'], item['age'], item['likes'])
# print(data)
#
# new_json = json.dumps(data, indent=2)
# print(type(new_json))
# print(new_json)

# with open('my.json', 'w') as file:
#     json.dump(new_json, file, indent=2)
# with open('my.json', 'r') as file:
#     data1 = json.load(file)
# print(data1)
# print(type(data1))
# data2 = json.loads(data1)
# print(type(data2))
# print(data2)
# for i in data2['response'].keys():
#     print(i)
# !!!!  decoding JSON -> Python
# object -> dict
# array ->list
# string -> str
# number(int) -> int
# number(real) -> float
# true -> True
# false -> False
# null -> None
message = "hello bro"
data = {
    "to_user": "Sergey",
    "text": message,
    "attachments": ["1.png", "2.wav"],
    "type": "direct"
}
print(type(data))
print(data)
json_string = json.dumps(data, indent=2)
print(json_string)
print(type(json_string))


class MyEncoder(json.JSONEncoder):  # create class which enherited of class json.JSONEncoder
    def default(self, o):  # redefine function default
        if isinstance(o, set):
            return list(o)
        return o


json_str2 = json.dumps({1, 2, 3}, cls=MyEncoder)  # cls = MyEncoder - for method dumps appointed cls MyEncoder

our_str = "hallo"
json_str3 = json.dumps(our_str)  # encode our Python str to JSON string
# we  can set False at  argument ensure_ascii, ensure_ascii=False,if string wrote not in English, and our encoding UTF8
# json_str3 = json.dumps(our_str,ensure_ascii=False)
# default value of argument sort_keys is False, if we want that Python during encoding to JSON string sorts keys ,
# set True , json_str3 = json.dumps(our_str, sort_keys=True)
print(type(json_str3))
print(json_str3)
json_str3 = json.dumps(our_str, sort_keys=True)

# json.dump('hello world', open('my.json', 'w', encoding='utf-8'), indent=2)
# print(json.load(open('my.json', 'r')))