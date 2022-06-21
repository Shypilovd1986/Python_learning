class Person():
    def __init__(self, name, age, strength):
        self.name = name
        self.age = age
        self.strength= strength

Sam = Person('Dmitriy', 32, 1200)
print(Sam.name)
print(type(Sam))