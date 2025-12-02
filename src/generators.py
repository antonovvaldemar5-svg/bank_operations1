def filter_by_currency(transactions, currency):
    """Фильтрует транзакции по валюте"""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency_info = operation_amount.get("currency", {})
        if currency_info.get("code") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генерирует описания транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """Генерирует номера карт в диапазоне"""
    for number in range(start, end + 1):
        card_str = str(number).zfill(16)
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted