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


@mock.patch.object(datetime.date, "today")
def test_valid_1(mocked_today):
    mocked_today.return_value = datetime.date(2020, 1, 15)
    assert outdated_products(tested_list) == ["test item"]


def test_valid_2():
    with mock.patch.object(datetime.date, "today") as mocked_today:
        mocked_today.return_value = datetime.date(2020, 1, 15)
        assert outdated_products(tested_list) == ["test item"]


def test_valid_3(monkeypatch):
    def mock_today():
        return datetime.date(2020, 1, 15)

    monkeypatch.setattr(datetime.date, "today", mock_today)
    assert outdated_products(tested_list) == ["test item"]
