import pytest
from tests.factories import BorrowFactory

pytestmark = pytest.mark.django_db


def test_borrow_list(auth_client):
    BorrowFactory.create_batch(2)

    response = auth_client.get("/api/borrowings/")

    assert response.status_code == 200
    assert len(response.data) == 2
