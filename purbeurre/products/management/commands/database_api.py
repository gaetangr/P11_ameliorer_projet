# flake8: noqa
import crayons
from django.conf import settings
from django.core.management.base import BaseCommand
from halo import Halo

from purbeurre.products.downloader import DataCleaner, Downloader
from purbeurre.products.models import Category, Product


class Command(BaseCommand):
    """Populate database with OpenFoodfacts Api"""

    help = """Populate database with OpenFoodfacts Api"""

    def handle(self, *args, **options):
        spinner = Halo(
            text="Fetching data and populating database...",
            text_color="yellow",
            spinner="dots",
        )
        spinner.start()

        Category.objects.all().delete()
        Product.objects.all().delete()

        downloader = Downloader()
        cleaner = DataCleaner()
        products = downloader.get_product(20, 20)
        categories, products = cleaner.clean(products)

        for cat in categories:
            Category.objects.create(name=cat)
        for product in products:
            name = product["product_name"]  # name
            image_url = product["image_url"]  # img url
            image_nutrition_url = product["image_nutrition_url"]
            url = product["url"]  # url product
            nutriscore_grade = product["nutriscore_grade"]  # nutriscore grade
            code = product["code"]

            product_instance = Product.objects.create(
                name=name,
                code=code,
                nutriscore_grade=nutriscore_grade,
                image_url=image_url,
                image_nutrition_url=image_nutrition_url,
                url=url,
            )
            for category in product["categories"]:
                category = Category.objects.get(name=category)
                product_instance.categories.add(category)

        spinner.succeed(crayons.green("Success!"))
