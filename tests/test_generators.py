import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100", "currency": {"code": "USD"}},
            "description": "Перевод 1"
        },
        {
            "id": 2,
            "operationAmount": {"amount": "200", "currency": {"code": "EUR"}},
            "description": "Перевод 2"
        },
        {
            "id": 3,
            "operationAmount": {"amount": "300", "currency": {"code": "USD"}},
            "description": "Перевод 3"
        }
    ]


def test_filter_by_currency(sample_transactions):
    """Тест фильтрации по валюте"""
    result = filter_by_currency(sample_transactions, "USD")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_transaction_descriptions(sample_transactions):
    """Тест получения описаний"""
    result = transaction_descriptions(sample_transactions)
    assert result == ["Перевод 1", "Перевод 2", "Перевод 3"]


def test_card_number_generator():
    """Тест генератора номеров карт"""
    result = card_number_generator(1, 3)
    expected = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    assert result == expected