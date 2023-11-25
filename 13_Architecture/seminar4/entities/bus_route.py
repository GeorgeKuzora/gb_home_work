from .bus_stop import BusStop


class BusRoute:
    def __init__(self, id: int, remark: str, capacity: int, bus_stops: list[BusStop]) -> None:
        self.id: int = id
        self.remark: str = remark
        self.capacity: int = capacity
        self.bus_stops: list[BusStop] = bus_stops
        
    def get_id(self) -> int:
        return self.id
    
    def get_remark(self) -> str:
        return self.remark
    
    def set_remark(self, remark: str) -> None:
        self.remark = remark
        
    def get_capacity(self) -> int:
        return self.capacity

    def set_capacity(self, capacity: int) -> None:
        self.capacity = capacity
        
    def get_bus_stops(self) -> list[BusStop]:
        return self.bus_stops
    
    def append_bus_stop(self, bus_stop: BusStop) -> None:
        self.bus_stops.append(bus_stop)

    def insert_bus_stop(self, bus_stop: BusStop, index: int) -> None:
        self.bus_stops.insert(index, bus_stop)
        
    def update_bus_stop(self, bus_stop: BusStop, index: int) -> None:
        self.bus_stops[index] = bus_stop
    
    def find_bus_stop(self, bus_stop_id: int) -> int:
        for i, bus_stop in enumerate(self.bus_stops):
            if bus_stop.get_id == bus_stop_id:
                return i
        raise ValueError("Остановка не входит в маршрут")