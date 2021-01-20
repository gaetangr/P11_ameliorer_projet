import factory.fuzzy

from ..models import User


class UserFactory(factory.django.DjangoModelFactory):
    """Generate fake data for user object"""

    username = factory.fuzzy.FuzzyText()
    password = factory.fuzzy.FuzzyText()
    bio = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)

    class Meta:
        model = User
