class Person:
    def __init__(
        self, id: int, fio: str, card_number: int, hash_pass: int, login: str
    ) -> None:
        self.id: int = id
        self.fio: str = fio
        self.card_number: int = card_number
        self.hash_pass: int = hash_pass
        self.login: str = login

    def get_id(self) -> int:
        return self.id

    def get_fio(self) -> str:
        return self.fio

    def get_login(self) -> str:
        return self.login

    def get_card_number(self) -> int:
        return self.card_number

    def set_login(self, login: str) -> None:
        self.login = login

    def get_hash_pass(self) -> int:
        return self.hash_pass

    def set_hash_pass(self, hash_pass: int) -> None:
        self.hash_pass = hash_pass
