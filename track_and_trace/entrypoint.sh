#!/bin/sh

python manage.py migrate --no-input

# Use sample data to seed shipment table
python manage.py seed_shipments shipment_sample.csv

exec "$@"