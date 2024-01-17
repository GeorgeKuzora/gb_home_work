from config import PlayersCharacters


class Player:
    def __init__(self) -> None:
        self.characters = None
        self.name = None

    def set_using_zeros(self) -> None:
        self.characters = PlayersCharacters.ZEROS

    def set_using_crosses(self) -> None:
        self.characters = PlayersCharacters.CROSSES

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_character_value(self) -> str:
        return self.characters.value