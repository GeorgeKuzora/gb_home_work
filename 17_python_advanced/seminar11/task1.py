from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author) -> None:
        instance = super().__new__(cls)
        instance.value = value
        instance.author = author
        instance.time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")
        return instance

    # def __init__(self, value, author) -> None:
    #     self.value = value
    #     self.author = author
    #     self.time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")

    def __str__(self) -> str:
        return f"{self.value} (Автор: {self.author}, Время создания: {self.time})"

    def __repr__(self) -> str:
        return f"MyStr('{self.value}', '{self.author}')"


if __name__ == "__main__":
    event = MyStr("Завершилось тестирование", "John")
    print(event)
    print(f"{event = }")
