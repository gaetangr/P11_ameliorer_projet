# flake8: noqa
""" Unit tests related to export/views"""
import pytest
from django.urls import reverse

from purbeurre.users.models import User


@pytest.mark.django_db
def test_if_csv_is_created_for_user(client):
    """Test if export view return correct 'content-type' and 'Content-Disposition' """
    user = User.objects.create_user(username="Gaetan")
    client.force_login(user)
    response = client.get("/exports/favorites/")
    assert (
        response.get("Content-Disposition")
        == f'attachment; filename="{user.username}_favorites.csv"'
    )
    assert response.get("content-type") == "text/csv"
