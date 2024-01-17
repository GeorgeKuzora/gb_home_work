class Cell:
    def __init__(self, initial_value: str) -> None:
        self.value = initial_value

    def get_value(self) -> str:
        return self.value
        
    def set_value(self, value) -> None:
        self.value = value

