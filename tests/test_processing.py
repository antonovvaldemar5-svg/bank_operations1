from src.processing import filter_by_state, sort_by_date
import pytest


# ФИКСТУРА - создает тестовые данные
@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-10T14:45:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-20T09:15:00.000000"},
    ]


# ПАРАМЕТРИЗАЦИЯ - один тест для разных данных
@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("PENDING", 0),
])
def test_filter_by_state_parametrized(sample_operations, state, expected_count):
    """Тестирует фильтрацию с разными статусами"""
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_count


def test_filter_by_state_default(sample_operations):
    """Тестирует фильтрацию со значением по умолчанию"""
    result = filter_by_state(sample_operations)
    assert len(result) == 2


def test_sort_by_date_newest_first(sample_operations):
    """Тестирует сортировку от новых к старым"""
    result = sort_by_date(sample_operations)
    assert result[0]["date"] == "2024-01-20T09:15:00.000000"

    def test_filter_by_state_empty_list():
        """Тест пустого списка операций"""
        result = filter_by_state([])
        assert result == []

    def test_sort_by_date_empty_list():
        """Тест сортировки пустого списка"""
        result = sort_by_date([])
        assert result == []