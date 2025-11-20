def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по валюте"""
    return [transaction for transaction in transactions
            if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code]

def transaction_descriptions(transactions):
    """Генератор описаний транзакций"""
    for transaction in transactions:
        yield transaction.get('description', '')

def card_number_generator(start, end):
    """Генератор номеров банковских карт"""
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        # Форматируем как XXXX XXXX XXXX XXXX
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted