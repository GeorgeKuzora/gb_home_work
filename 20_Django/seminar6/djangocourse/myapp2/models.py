from datetime import date

from django.core.validators import MinValueValidator
from django.db import models


class Client(models.Model):
    name = models.CharField("Name", max_length=100)
    email = models.EmailField("Email", max_length=100, unique=True)
    phone_number = models.CharField("Phone number", max_length=12)
    address = models.CharField("Address", max_length=200)
    registration_date = models.DateField("Registration date", default=date.today())

    def __str__(self):
        return f"{self.name}, {self.email}, {self.phone_number}"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(1)])
    qnt = models.IntegerField(validators=[MinValueValidator(0)])
    creation_date = models.DateField("Creation date", default=date.today())
    image = models.ImageField("Image of product", null=True)

    def __str__(self):
        return f"{self.title}: {self.price}"


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="order")
    total_price = models.IntegerField(validators=[MinValueValidator(1)])
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}: {self.products}"
