from datetime import date
from typing import Any

from django.core.management.base import BaseCommand

from myapp2.models import Client, Order, Product


class Command(BaseCommand):
    help = "Creates orders in database"

    def handle(self, *args: Any, **options: Any) -> str | None:
        client = Client.objects.filter().first()
        products = Product.objects.all()
        order = Order(
            customer=client,
            total_price=200000,
            date_ordered=date(year=2024, month=4, day=1),
        )
        order.save()
        for product in products:
            if product:
                order.products.add(product)
        order.save()
        self.stdout.write(f"{order}")
