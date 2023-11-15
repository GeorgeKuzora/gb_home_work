from .poligon import Poligon
from .texture import Texture


class PoligonalModel:
    def __init__(self, texture: list[Texture]) -> None:
        self.poligons: list[Poligon] = [Poligon()]
        self.texture: list[Texture] = texture
