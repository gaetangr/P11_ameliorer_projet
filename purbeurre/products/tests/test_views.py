# flake8: noqa
""" Unit tests related to users/views"""
import pytest
from django.urls import reverse
from django.test import Client

from purbeurre.products.models import Category, Product
from purbeurre.users.tests.factories import UserFactory

from .factories import ProductFactory


@pytest.fixture
def user():
    """Create a new user object with abstract datas

    Returns:
        class: Return user factory
    """
    return UserFactory


@pytest.fixture
def product():
    """Create a new product object with abstract datas

    Returns:
        class: Return product factory
    """
    return ProductFactory


@pytest.mark.django_db
def test_if_detail_view_can_be_access_by_user(client, user, product):
    """Test if a product detail view can be access by a user """
    user = user
    product = product
    url = reverse("products:detail", kwargs={"pk": product.pk})
    assert url == reverse("products:detail", kwargs={"pk": product.pk})


@pytest.mark.django_db
def test_if_no_product_provided_should_return_redirect(client):
    """If not input from user, should redirect and not display page """
    url = reverse("products:prod")
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_if_product_is_search_ajax_should_return_200():
    """If user input search product, autocomplete should return 200 and return product"""
    Product.objects.create(name="Nutella")
    c = Client(enforce_csrf_checks=True)
    response = c.get('/products/get_product/', {'term': 'Nutella'})
    assert response.content == b'["Nutella"]'
    assert response.status_code == 200