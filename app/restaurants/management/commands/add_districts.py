from django.core.management.base import BaseCommand

from ...models import District


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        with open(f"list/district_list.txt") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                District.objects.get_or_create(
                    name=name,
                )
        self.stdout.write(self.style.SUCCESS("list of districts added"))
