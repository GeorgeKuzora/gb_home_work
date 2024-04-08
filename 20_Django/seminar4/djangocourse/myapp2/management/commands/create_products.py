from datetime import date
from typing import Any

from django.core.management.base import BaseCommand

from myapp2.models import Product


class Command(BaseCommand):
    help = "Creates products in database"

    def handle(self, *args: Any, **options: Any) -> str | None:
        product = Product(
            title="computer",
            description="Nice computer",
            price=100000,
            qnt=2,
            creation_date=date(year=2024, month=4, day=1),
        )
        product.save()
        self.stdout.write(f"{product}")
