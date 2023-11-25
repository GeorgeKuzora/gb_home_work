class TransportZone:
    def __init__(self, id: int, remark: str) -> None:
        self.id: int = id
        self.remark: str = remark
        
    def get_id(self) -> int:
        return self.id
    
    def get_remark(self) -> str:
        return self.remark
    
    def set_remark(self, remark: str) -> None:
        self.remark = remark