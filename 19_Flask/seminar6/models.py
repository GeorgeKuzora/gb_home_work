import databases
import sqlalchemy

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("surname", sqlalchemy.String(100)),
    sqlalchemy.Column("password", sqlalchemy.String(100)),
)

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("description", sqlalchemy.String(1000)),
    sqlalchemy.Column("price", sqlalchemy.Integer),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("user.id")),
    sqlalchemy.Column("item_id", sqlalchemy.ForeignKey("item.id")),
    sqlalchemy.Column("date", sqlalchemy.DateTime),
    sqlalchemy.Column("status", sqlalchemy.String(10)),
)
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
