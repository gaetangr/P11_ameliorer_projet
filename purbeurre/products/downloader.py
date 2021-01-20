"""Module to Request data from OpenFoodFact."""

import requests


class Downloader:
    """Download products from OpenFoodFacts/API."""

    def __init__(self):
        """Url : Takes the url from which the date is received
        Params : Takes parametres to filter the query"""
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.params = {
            "action": "process",
            "sort_by": "unique_scans_n",
            "page_size": None,
            "json": 1,
            "page": 1,
            "fields": "nutriscore_grade,product_name,url,code,categories,image_url,image_nutrition_url",
        }

    def get_product(self, page_size=10, pages_number=1):
        """Display product based on specifics parameters.

        Args:
            page_size (int, optional): Number of products. Defaults to 20.
            pages_number (int, optional): Page number to get products. Defaults to 1.

        Returns:
            list: Return a list of products
        """
        products = []
        params = self.params.copy()
        params["page_size"] = page_size

        try:
            response = requests.get(self.url, params=params, timeout=3)
            response.json()
        except requests.ConnectionError:
            print("Error when fetching the API")
        for i in range(pages_number):
            params["page"] = i + 1
            response = requests.get(self.url, params=params)
            if response.status_code == 200:
                products.extend(response.json()["products"])
        return products


class DataCleaner:
    """Clean the data received from the API."""

    def is_valid(self, product):
        if (
            product.get("nutriscore_grade")
            and product.get("product_name")
            and product.get("url")
            and product.get("image_url")
            and product.get("image_nutrition_url")
            and product.get("code")
            and product.get("categories")
        ):
            return True

    def clean(self, products):
        """Parse and normalize data from the API

        Args:
            products (list): products received from the API

        Returns:
            list: Return a list of clean products
        """
        clean_products = []
        clean_categories = set()
        for product in products:
            if self.is_valid(product):
                product["categories"] = [
                    cat.strip().lower().capitalize()
                    for cat in product["categories"].split(",")
                ]
                clean_products.append(product)
                clean_categories |= set(product["categories"])
        return clean_categories, clean_products


""" downloader = Downloader()
cleaner = DataCleaner()

products = downloader.get_product()
categories, products = cleaner.clean(products)

for product in products:
    print(

    product["image_url"],
    product["categories"]) """
