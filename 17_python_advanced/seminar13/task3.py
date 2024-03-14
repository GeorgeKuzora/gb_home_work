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

    def get_age(self):
        return self.age


class Employee(Person):
    ids = set()

    def __init__(self, surname, name, parentname, age, id):
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


person = Person("", "John", "Doe", 30)
print(person)
