from django.core.management.base import BaseCommand
from dashboard.models import ShopData
import csv
import os

class Command(BaseCommand):
    help = 'Importuje dane z shop_clean.csv do modelu ShopData'

    def add_arguments(self, parser):
        parser.add_argument('--csv', type=str, default=None, help='Ścieżka do pliku CSV')

    def handle(self, *args, **options):
        # Ustal ścieżkę bazową projektu
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        default_csv = os.path.join(BASE_DIR, 'Flask_app', 'data', 'processed', 'shop_clean.csv')
        csv_path = options['csv'] or default_csv
        self.stdout.write(f'Importuję dane z: {csv_path}')
        if not os.path.exists(csv_path):
            self.stderr.write(self.style.ERROR(f'Plik nie istnieje: {csv_path}'))
            return
        with open(csv_path, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            ShopData.objects.all().delete()
            count = 0
            for row in reader:
                ShopData.objects.create(
                    ad_group=row['ad_group'],
                    month=row['month'],
                    impressions=int(row['impressions']),
                    clicks=int(row['clicks']),
                    ctr=float(row['ctr']),
                    conversions=int(row['conversions']),
                    conv_rate=float(row['conv_rate']),
                    cost=float(row['cost']),
                    cpc=float(row['cpc']),
                    revenue=float(row['revenue']),
                    sale_amount=float(row['sale_amount']),
                    pandl=float(row['pandl'])
                )
                count += 1
        self.stdout.write(self.style.SUCCESS(f'Zaimportowano {count} rekordów.'))
