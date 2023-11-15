from model_elements.camera import Camera
from model_elements.flash import Flash
from model_elements.poligonal_model import PoligonalModel


class Scene[T]:
    def __init__(
        self, models: list[PoligonalModel], flashes: list[Flash], cameras: list[Camera]
    ) -> None:
        self.id: int = 0
        self.models: list[PoligonalModel] = models
        self.flashes: list[Flash] = flashes

    def method1(self, object: T) -> T:
        return object

    def method2(self, object1: T, object2: T) -> T:
        return object1
