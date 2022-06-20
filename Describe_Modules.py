# ***********    module random    ***********
# from random import randint
# randint(1,200)  takes random numbers from range of values 1 - 200
# random()  returns random number from 0 to  1
# shuffle(a), shuffles mutable sequence a
#
# ************   os     *************
# import os
# os.mkdir('C:\\m1')    -   create file m1
# print(os.path.exists('C:\\m1'))   return True if file exists or False if not

# *************      json       *****************
# import json
# from random import randint

# JSON  -JavaScript Object Notation, A common use of JSON is to read data from a web server, and display the data in a
# web page. Применяется в веб-приложениях как для обмена данными между браузером и сервером (AJAX), так и между
# серверами (программные HTTP-сопряжения).
# !!!!!!!  use only double quotes not single
# str_json = строка из джейсона
# data = json.loads(str_json)   - переведет из строки джейсон в словарь
# new_json = json.dumps(data, indent=2) переведет словарь в строку джейсон


# with open('my.json', 'w') as file:
#     json.dump(new_json, file, indent=2)    создаст и запишет в файл джейсон нашу строку
# with open('my.json', 'r') as file:
#     data1 = json.load(file)               считает нашу строку из джейсона
# !!!!  decoding JSON -> Python
# object -> dict
# array ->list
# string -> str
# number(int) -> int
# number(real) -> float
# true -> True
# false -> False
# null -> None
