class BusStop:
    def __init__(self, id: int, name: str, altitude: int, latitude: int) -> None:
        self.id: int = id
        self.name: str = name
        self.altitude: int = altitude
        self.latitude: int = latitude
        
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
        
    def get_coordinates(self) -> tuple[int, int]:
        coordinates: tuple[int, int] = (self.altitude, self.latitude)
        return coordinates
    
    def set_coordinates(self, altitude: int, latitude: int) -> None:
        self.altitude = altitude
        self.latitude = latitude