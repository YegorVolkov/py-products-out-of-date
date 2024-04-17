from unittest import mock
from app.main import outdated_products, datetime

tested_list = [
    {"name": "test item",
     "expiration_date": datetime.date(2020, 1, 15),
     "price": 100}
]


@mock.patch("datetime.date.today")
def test_valid(mocked_today):
    mocked_today.return_value = datetime.date(2020, 1, 15)
    assert outdated_products(tested_list) == ["test item"]


@mock.patch("datetime.date.today")
def test_expired(mocked_today):
    mocked_today.return_value = datetime.date(2020, 1, 16)
    assert outdated_products(tested_list) is None
