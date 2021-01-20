from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from purbeurre.products.models import Product


class User(AbstractUser):
    """Stores a profile, a profile is related to an instance of :model:`auth.User`

    Args:
        AbstractUser : An abstract base class for extending user model
    """

    bio = models.TextField(
        "Bio",
        blank=True,
        help_text=_("Tell the world about yourself, what products do you like etc."),
    )

    def get_absolute_url(self):
        """If model is created, return user to specific path"""
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        """Return object with an explicit string name"""
        return self.username


class Favorite(models.Model):
    """Stores a favoris, a favoris is related to an instance of :model:`auth.User`

    Args:
        AbstractUser : An abstract base class for extending user model
    """

    # Required fields
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorite_users"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="favorite_product"
    )
    substitute = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="favorite_substitute"
    )

    def __str__(self):
        """Return object with an explicit string name"""
        return f"Product : {self.product} ---> Substitut : {self.substitute}"
