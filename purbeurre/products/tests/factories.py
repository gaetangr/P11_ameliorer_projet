import factory.fuzzy

from ..models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    """Generate fake data for product object"""

    pk = 0
    code = factory.fuzzy.FuzzyText()
    name = factory.fuzzy.FuzzyText()
    nutriscore_grade = factory.fuzzy.FuzzyText(length=1)
    url = factory.fuzzy.FuzzyText()
    image_url = factory.fuzzy.FuzzyText()

    class Meta:
        model = Product
