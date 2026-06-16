from pydantic import BaseModel


class CityModel(BaseModel):
    name: str
    currency: str
    gasoline: float
    midGrade: float
    premium: float
    diesel: float


class StateModel(BaseModel):
    name: str
    gasoline: float
    midGrade: float
    premium: float
    diesel: float
