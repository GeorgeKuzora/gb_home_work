from typing import List

from fastapi import FastAPI

import models
import validators

app = FastAPI()


@app.on_event("startup")
async def startup():
    await models.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await models.database.disconnect()


@app.post("/users/", response_model=validators.User)
async def create_user(user: validators.UserIn):
    query = models.users.insert().values(
        name=user.name, surname=user.surname, email=user.email, password=user.password
    )
    last_record_id = await models.database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.get("/users/", response_model=List[validators.User])
async def read_users():
    query = models.users.select()
    return await models.database.fetch_all(query)


@app.get("/users/{user_id}", response_model=validators.User)
async def read_user(user_id: int):
    query = models.users.select().where(models.users.c.id == user_id)
    return await models.database.fetch_one(query)


@app.put("/users/{user_id}", response_model=validators.User)
async def update_user(user_id: int, new_user: validators.UserIn):
    query = (
        models.users.update()
        .where(models.users.c.id == user_id)
        .values(**new_user.dict())
    )
    await models.database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = models.users.delete().where(models.users.c.id == user_id)
    await models.database.execute(query)
    return {"message": "User deleted"}


@app.post("/items/", response_model=validators.Item)
async def create_item(item: validators.ItemIn):
    query = models.items.insert().values(
        name=item.name, description=item.description, price=item.price
    )
    last_record_id = await models.database.execute(query)
    return {**item.dict(), "id": last_record_id}


@app.get("/items/", response_model=List[validators.Item])
async def read_items():
    query = models.items.select()
    return await models.database.fetch_all(query)


@app.get("/items/{item_id}", response_model=validators.Item)
async def read_item(item_id: int):
    query = models.items.select().where(models.items.c.id == item_id)
    return await models.database.fetch_one(query)


@app.put("/items/{item_id}", response_model=validators.Item)
async def update_item(item_id: int, new_item: validators.ItemIn):
    query = (
        models.items.update()
        .where(models.items.c.id == item_id)
        .values(**new_item.dict())
    )
    await models.database.execute(query)
    return {**new_item.dict(), "id": item_id}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = models.items.delete().where(models.items.c.id == item_id)
    await models.database.execute(query)
    return {"message": "Item deleted"}


@app.post("/orders/", response_model=validators.Order)
async def create_order(order: validators.OrderIn):
    query = models.orders.insert().values(
        order_id=order.user_id,
        item_id=order.item_id,
        date=order.date,
        status=order.status,
    )
    last_record_id = await models.database.execute(query)
    return {**order.dict(), "id": last_record_id}


@app.get("/orders/", response_model=List[validators.Order])
async def read_orders():
    query = models.orders.select()
    return await models.database.fetch_all(query)


@app.get("/orders/{order_id}", response_model=validators.Order)
async def read_order(order_id: int):
    query = models.orders.select().where(models.orders.c.id == order_id)
    return await models.database.fetch_one(query)


@app.put("/orders/{order_id}", response_model=validators.Order)
async def update_order(order_id: int, new_order: validators.OrderIn):
    query = (
        models.orders.update()
        .where(models.orders.c.id == order_id)
        .values(**new_order.dict())
    )
    await models.database.execute(query)
    return {**new_order.dict(), "id": order_id}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = models.orders.delete().where(models.orders.c.id == order_id)
    await models.database.execute(query)
    return {"message": "Order deleted"}
