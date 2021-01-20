# flake8: noqa
""" Unit tests related to users/views"""
import pytest
from django.urls import reverse

from .factories import UserFactory


@pytest.fixture
def user():
    """Create a new user object with abstract datas

    Returns:
        class: Return user factory
    """
    return UserFactory


@pytest.mark.django_db
def test_if_get_redirect_return_username_name_of_user(client, user):
    """Test if the Login views return a 200 response """
    user = user
    url = reverse("users:detail", kwargs={"username": user.username})
    assert url == reverse("users:detail", kwargs={"username": user.username})


@pytest.mark.django_db
def test_if_login_views_is_successful(client):
    """Test if the Login views return a 200 response """

    url = reverse("users:login")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_if_fav_views_is_unsuccessful_for_anonymous(client):
    """View should redirect anonymous user if he tries to access protected page """

    url = reverse("users:fav", kwargs={"username": "anonymous"})
    response = client.get(url)
    assert response.status_code == 302


# Extra tests to assert some pages return 200 response and that admin page are
# not available for regular users
# ------------------------------------------------------------------------------


@pytest.mark.django_db
def test_if_home_is_successful(client):
    """Test if the home return a 200 response """

    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200


def test_if_a_superuser_can_access_administration_panel(admin_client):
    """Test if a superuser can access the administration panel while being login
    :param admin_client: An instance of a superuser, with username “admin” and password “password” to test admin .
    """
    response = admin_client.get("/admin/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_if_an_user_c_access_administration_panel(client):
    """Test if a none superuser is fordbiden to access to the administration panel while being login
    :param client: An instance of a django.test.Client with no superuser privilegies
    """
    response = client.get("/admin/")
    assert response.status_code != 200
