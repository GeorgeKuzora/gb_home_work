Общая статистика

Всего тестов: 4. Пройдено: 2. Не пройдено: 2.

Подробную информацию по каждому тесту смотрите ниже.
Тест 1
Тест пройден успешно ✓

Формулировка:

* Итоговый код для проверки.

import warnings

warnings.filterwarnings('ignore')

class InvalidNameError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid name: {self.value}. Name should be a non-empty string."


class InvalidAgeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid age: {self.value}. Age should be a positive integer."


class InvalidIdError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid id: {self.value}. Id should be a 6-digit positive integer between 100000 and 999999."


class Name:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name, "")

    def __set__(self, obj, value: str):
        if not (value and isinstance(value, str)):
            raise InvalidNameError(value)
        obj.__dict__[self.name] = value


class Person:
    surname = Name()
    name = Name()
    parentname = Name()

    def __init__(self, surname, name, parentname, age):
        self.surname = surname
        self.name = name
        self.parentname = parentname
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (isinstance(value, int) and value > 0):
            raise InvalidAgeError(value)
        self._age = value

    def birthday(self):
        self.age += 1


class Employee(Person):
    ids = set()

    def __init__(self, surname, name, parentname, id, age):
        self.id = id
        super().__init__(surname, name, parentname, age)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not (
            isinstance(value, int)
            and value >= 100000
            and value <= 999999
            and value not in self.ids
        ):
            raise InvalidIdError(value)
        self._id = value
        self.ids.add(value)

    def get_level(self):
        return self.id % 7

#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#person = Person("", "John", "Doe", 30)
#print(person) 


person = Person("", "John", "Doe", 30)




print()

Тест 2
Тест пройден успешно ✓

Формулировка:

* Итоговый код для проверки.

import warnings

warnings.filterwarnings('ignore')

class InvalidNameError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid name: {self.value}. Name should be a non-empty string."


class InvalidAgeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid age: {self.value}. Age should be a positive integer."


class InvalidIdError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid id: {self.value}. Id should be a 6-digit positive integer between 100000 and 999999."


class Name:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name, "")

    def __set__(self, obj, value: str):
        if not (value and isinstance(value, str)):
            raise InvalidNameError(value)
        obj.__dict__[self.name] = value


class Person:
    surname = Name()
    name = Name()
    parentname = Name()

    def __init__(self, surname, name, parentname, age):
        self.surname = surname
        self.name = name
        self.parentname = parentname
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (isinstance(value, int) and value > 0):
            raise InvalidAgeError(value)
        self._age = value

    def birthday(self):
        self.age += 1


class Employee(Person):
    ids = set()

    def __init__(self, surname, name, parentname, id, age):
        self.id = id
        super().__init__(surname, name, parentname, age)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not (
            isinstance(value, int)
            and value >= 100000
            and value <= 999999
            and value not in self.ids
        ):
            raise InvalidIdError(value)
        self._id = value
        self.ids.add(value)

    def get_level(self):
        return self.id % 7

#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#person = Person("", "John", "Doe", 30)
#print(person) 


person = Person("Alice", "Smith", "Johnson", -5)




print()

Тест 3
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.

import warnings

warnings.filterwarnings('ignore')

class InvalidNameError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid name: {self.value}. Name should be a non-empty string."


class InvalidAgeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid age: {self.value}. Age should be a positive integer."


class InvalidIdError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid id: {self.value}. Id should be a 6-digit positive integer between 100000 and 999999."


class Name:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name, "")

    def __set__(self, obj, value: str):
        if not (value and isinstance(value, str)):
            raise InvalidNameError(value)
        obj.__dict__[self.name] = value


class Person:
    surname = Name()
    name = Name()
    parentname = Name()

    def __init__(self, surname, name, parentname, age):
        self.surname = surname
        self.name = name
        self.parentname = parentname
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (isinstance(value, int) and value > 0):
            raise InvalidAgeError(value)
        self._age = value

    def birthday(self):
        self.age += 1


class Employee(Person):
    ids = set()

    def __init__(self, surname, name, parentname, id, age):
        self.id = id
        super().__init__(surname, name, parentname, age)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not (
            isinstance(value, int)
            and value >= 100000
            and value <= 999999
            and value not in self.ids
        ):
            raise InvalidIdError(value)
        self._id = value
        self.ids.add(value)

    def get_level(self):
        return self.id % 7

#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#person = Person("", "John", "Doe", 30)
#print(person) 


employee = Employee("Bob", "Johnson", "Brown", 40, 12345)




print()



Ожидаемый ответ:

__main__.InvalidIdError: Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999.

Ваш ответ:

__main__.InvalidIdError: Invalid id: 40. Id should be a 6-digit positive integer between 100000 and 999999.
Тест 4
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.

import warnings

warnings.filterwarnings('ignore')

class InvalidNameError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid name: {self.value}. Name should be a non-empty string."


class InvalidAgeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid age: {self.value}. Age should be a positive integer."


class InvalidIdError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Invalid id: {self.value}. Id should be a 6-digit positive integer between 100000 and 999999."


class Name:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name, "")

    def __set__(self, obj, value: str):
        if not (value and isinstance(value, str)):
            raise InvalidNameError(value)
        obj.__dict__[self.name] = value


class Person:
    surname = Name()
    name = Name()
    parentname = Name()

    def __init__(self, surname, name, parentname, age):
        self.surname = surname
        self.name = name
        self.parentname = parentname
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (isinstance(value, int) and value > 0):
            raise InvalidAgeError(value)
        self._age = value

    def birthday(self):
        self.age += 1


class Employee(Person):
    ids = set()

    def __init__(self, surname, name, parentname, id, age):
        self.id = id
        super().__init__(surname, name, parentname, age)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not (
            isinstance(value, int)
            and value >= 100000
            and value <= 999999
            and value not in self.ids
        ):
            raise InvalidIdError(value)
        self._id = value
        self.ids.add(value)

    def get_level(self):
        return self.id % 7

#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#person = Person("", "John", "Doe", 30)
#print(person) 


person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())



Ожидаемый ответ:

25

Ошибка:

Traceback (most recent call last):
  File "3P6S663CNKXF3N5IY0TP.py", line 104, in <module>
    print(person.get_age())
AttributeError: 'Person' object has no attribute 'get_age'
 
