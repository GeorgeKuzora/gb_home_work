from datetime import date


class Ticket:
    def __init__(
        self,
        price: int,
        valid_on_date: date,
        start_zone: int,
        finish_zone: int,
        is_luggage: bool,
        place: int,
        road_number: int,
    ) -> None:
        self.price: int = price
        self.valid_on_date: date = valid_on_date
        self.start_zone: int = start_zone
        self.finish_zone: int = finish_zone
        self.is_luggage: bool = is_luggage
        self.place: int = place
        self.road_number: int = road_number
        
    def get_price(self) -> int:
        return self.price
    
    def get_valid_on_date(self) -> date:
        return self.valid_on_date

    def get_start_zone(self) -> int:
        return self.start_zone
    
    def get_finish_zone(self) -> int:
        return self.finish_zone
    
    def get_is_luggage(self) -> bool:
        return self.is_luggage
    
    def get_place(self) -> int:
        return self.place
    
    def get_road_number(self) -> int:
        return self.road_number