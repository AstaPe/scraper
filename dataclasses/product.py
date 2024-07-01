from dataclasses import dataclass


@dataclass
class InternetPlan:
    name: str
    price: float
    speed: int
    company:str
    