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
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    # Преобразуем итератор в список для проверки
    result = list(usd_transactions)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_transaction_descriptions(sample_transactions):
    """Тест генератора описаний"""
    descriptions = transaction_descriptions(sample_transactions)
    result = list(descriptions)
    assert result == ["Перевод 1", "Перевод 2", "Перевод 3"]


def test_card_number_generator():
    """Тест генератора номеров карт"""
    cards = card_number_generator(1, 3)
    result = list(cards)
    expected = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    assert result == expected


def test_generators_are_iterators():
    """Тест что функции возвращают итераторы"""
    transactions = [{"operationAmount": {"currency": {"code": "USD"}}, "description": "Test"}]

    # Проверяем что это генераторы (итераторы)
    usd = filter_by_currency(transactions, "USD")
    desc = transaction_descriptions(transactions)
    cards = card_number_generator(1, 1)

    # Должны работать с next()
    assert next(usd) is not None
    assert next(desc) == "Test"
    assert next(cards) == "0000 0000 0000 0001"