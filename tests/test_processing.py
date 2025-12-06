from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state():
    """Тест фильтрации по статусу"""
    transactions = [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00.000"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00.000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00.000"},
        {"id": 4, "state": "PENDING", "date": "2024-01-04T00:00:00.000"}
    ]

    result = filter_by_state(transactions, "EXECUTED")
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)


def test_sort_by_date():
    """Тест сортировки по дате"""
    transactions = [
        {"id": 1, "date": "2024-01-01T00:00:00.000"},
        {"id": 2, "date": "2024-01-03T00:00:00.000"},
        {"id": 3, "date": "2024-01-02T00:00:00.000"}
    ]

    result_desc = sort_by_date(transactions, reverse=True)
    assert result_desc[0]["id"] == 2
    assert result_desc[1]["id"] == 3
    assert result_desc[2]["id"] == 1


def test_sort_by_date_with_timezones():
    """Тест сортировки с временными зонами"""
    transactions = [
        {"id": 1, "date": "2024-01-01T10:00:00.000Z"},
        {"id": 2, "date": "2024-01-01T15:00:00.000Z"},
        {"id": 3, "date": "2024-01-01T10:00:00.000"},
        {"id": 4, "date": "2024-01-01T15:00:00.000"}
    ]

    result = sort_by_date(transactions)
    assert len(result) == 4
