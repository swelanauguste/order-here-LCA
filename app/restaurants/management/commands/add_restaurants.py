import random

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Category, District, Restaurant


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        fake = Faker()

        for _ in range(20):
            Restaurant.objects.get_or_create(
                name=fake.company(),
                category=Category.objects.get(pk=random.randint(1, 4)),
                district=District.objects.get(pk=random.randint(1, 9)),
                email=fake.profile()["mail"],
                tel1=fake.phone_number(),
                tel2=fake.phone_number(),
            )
        self.stdout.write(self.style.SUCCESS("list of restaurants added"))
