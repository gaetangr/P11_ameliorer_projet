import pytest

from purbeurre.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url():
    """Method `get_absolute_url`should return username """
    user = User.objects.create_user(username="Gaetan")
    assert user.get_absolute_url() == f"/users/{user.username}/"


def test__str__():
    """If an user object is created, it should return the object with username"""
    user = User.objects.create(
        username="Ratatouille",
        bio="Semi-sweet cheese that goes well with starches.",
    )

    assert user.__str__() == "Ratatouille"
    assert str(user) == "Ratatouille"
