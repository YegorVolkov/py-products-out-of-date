from unittest import mock
from app.main import outdated_products, datetime

tested_list = [
    {"name": "test item",
     "expiration_date": datetime.date(2020, 1, 15),
     "price": 100}
]


@mock.patch("datetime.date.today")
def test_valid(mocked_today: mock.patch) -> None:
    mocked_today.return_value = datetime.date(2020, 1, 14)
    assert outdated_products(tested_list) == ["test item"]


@mock.patch.object(datetime.date, "today")
def test_valid_1(mocked_today: mock.patch.object) -> None:
    mocked_today.return_value = datetime.date(2020, 1, 14)
    assert outdated_products(tested_list) == ["test item"]


def test_valid_2() -> None:
    with mock.patch.object(datetime.date, "today") as mocked_today:
        mocked_today.return_value = datetime.date(2020, 1, 14)
        assert outdated_products(tested_list) == ["test item"]


def test_valid_3(monkeypatch: mock) -> None:
    def mock_today() -> datetime:
        return datetime.date(2020, 1, 14)

    monkeypatch.setattr(datetime.date, "today", mock_today)
    assert outdated_products(tested_list) == ["test item"]
