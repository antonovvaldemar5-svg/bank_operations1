from src.generators import card_number_generator, filter_by_currency
from src.generators import transaction_descriptions


def test_filter_by_currency():
    """Тест фильтрации транзакций по валюте"""
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}},
        {"operationAmount": {"currency": {"code": "EUR"}, "amount": "200"}},
        {"operationAmount": {"currency": {"code": "USD"}, "amount": "300"}},
    ]

    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"
    assert result[1]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_empty():
    """Тест фильтрации пустого списка"""
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_filter_by_currency_no_match():
    """Тест когда нет совпадений по валюте"""
    transactions = [
        {"operationAmount": {"currency": {"code": "EUR"}, "amount": "100"}}
    ]

    result = list(filter_by_currency(transactions, "USD"))
    assert result == []


def test_transaction_descriptions():
    """Тест генератора описаний транзакций"""
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Оплата услуг"},
        {"description": "Снятие наличных"},
    ]

    generator = transaction_descriptions(transactions)
    descriptions = list(generator)

    expected = ["Перевод организации", "Оплата услуг", "Снятие наличных"]
    assert descriptions == expected


def test_card_number_generator_single():
    """Тест генератора с одним номером"""
    generator = card_number_generator(5, 5)
    numbers = list(generator)

    assert numbers == ["0000 0000 0000 0005"]


def test_card_number_generator_range():
    """Тест генератора с большим диапазоном"""
    generator = card_number_generator(9999999999999990, 9999999999999993)
    numbers = list(generator)

    expected = [
        "9999 9999 9999 9990",
        "9999 9999 9999 9991",
        "9999 9999 9999 9992",
        "9999 9999 9999 9993"
    ]
    assert numbers == expected
