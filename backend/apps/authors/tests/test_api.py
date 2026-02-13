import pytest
from tests.factories import AuthorFactory

pytestmark = pytest.mark.django_db


def test_authors_list(auth_client):
    AuthorFactory.create_batch(2)

    response = auth_client.get("/api/authors/")

    assert response.status_code == 200
    assert len(response.data) == 2
