from datetime import date
from typing import Any

from django.core.management.base import BaseCommand

from myapp2.models import Client


class Command(BaseCommand):
    help = "Creates clients in database"

    def handle(self, *args: Any, **options: Any) -> str | None:
        client = Client(
            name="John",
            email="John@john.com",
            phone_number="+79219311126",
            address="Moscow, Red square",
            registration_date=date(year=2024, month=4, day=1),
        )
        client.save()
        self.stdout.write(f"{client}")
