from shop_backend.models import Item
from django.core.management.base import BaseCommand
import csv
from os import path

class Command(BaseCommand):
    def handle(self, **options):
        Item.objects.all().delete()
        base_directory = path.abspath(path.join(__file__,'../../../..'))
        with open(f'{base_directory}/data/wholefoodsorders.csv', 'r') as csvdata:
            data = list(csv.reader(csvdata))
            for item in data[1:]:
                Item(product_name = item[1],
                    company_name = item[0],
                    reg_price = item[2],
                    sale_price = item[3] if item[3] != '0' else item[4],
                    category = item[5]).save()