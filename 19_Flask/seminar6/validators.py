from datetime import datetime

from pydantic import BaseModel, Field


class ItemIn(BaseModel):
    name: str = Field(title="Name", max_length=50)
    description: str = Field(title="Description", max_length=1000)
    price: int = Field(title="Price", gt=0)


class Item(BaseModel):
    id: int = Field(title="ID", ge=0)
    name: str = Field(title="Name", max_length=50)
    description: str = Field(title="Description", max_length=1000)
    price: int = Field(title="Price", gt=0)


class UserIn(BaseModel):
    name: str = Field(title="Name", max_length=50)
    surname: str = Field(title="Surname", max_length=100, default="")
    email: str = Field(title="Email", max_length=100)
    password: str = Field(title="Password", min_length=8, max_length=100)


class User(BaseModel):
    id: int = Field(title="ID", ge=0)
    name: str = Field(title="Name", max_length=50)
    surname: str = Field(title="Surname", max_length=100, default="")
    email: str = Field(title="Email", max_length=100)
    password: str = Field(title="Password", min_length=8, max_length=100)


class OrderIn(BaseModel):
    user_id: int = Field(title="User")
    item_id: int = Field(title="Item")
    date: datetime = Field(title="Date", default=datetime.now())
    status: str = Field(title="Status", max_length=10)


class Order(BaseModel):
    id: int = Field(title="ID", ge=0)
    user_id: int = Field(title="User")
    item_id: int = Field(title="Item")
    date: datetime = Field(title="Date", default=datetime.now())
    status: str = Field(title="Status", max_length=10)
