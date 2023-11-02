import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from pathlib import Path
import csv
from django.db import IntegrityError

# local imports
from tracking.models import Shipment, StatusOptions, Location


class Command(BaseCommand):
    help = "Seed shipment table with provided csv file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file_path", type=Path)

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.MIGRATE_LABEL("Seeding shipment table...")
        )

        shipment_sample_data_path: Path = options["csv_file_path"].resolve()

        with open(shipment_sample_data_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:

                sender_location = Location.from_address(row["sender_address"])
                receiver_location = Location.from_address(row["receiver_address"])

                shipment = Shipment.objects.create(
                    tracking_number=row["tracking_number"],
                    carrier=row["carrier"],
                    sender_address=sender_location,
                    receiver_address=receiver_location,
                    article_name=row["article_name"],
                    article_quantity=row["article_quantity"],
                    article_price=row["article_price"],
                    sku=row["SKU"],
                    status=StatusOptions(row["status"]),
                )
                self.stdout.write(self.style.SUCCESS(f"{shipment} Added."))
