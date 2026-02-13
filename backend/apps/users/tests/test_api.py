import pytest
from tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_users_list(auth_client):
    UserFactory.create_batch(2)

    response = auth_client.get("/api/users/")

    assert response.status_code == 200
