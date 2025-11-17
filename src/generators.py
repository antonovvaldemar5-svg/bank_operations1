from typing import List, Dict


def filter_by_currency(transactions: List[Dict], currency: str) -> List[Dict]:
    """Фильтрует транзакции по валюте"""
    result = []
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency_info = operation_amount.get("currency", {})
        if currency_info.get("code") == currency:
            result.append(transaction)
    return result


def transaction_descriptions(transactions: List[Dict]) -> List[str]:
    """Возвращает описания транзакций"""
    result = []
    for transaction in transactions:
        result.append(transaction["description"])
    return result


def card_number_generator(start: int, end: int) -> List[str]:
    """Генерирует номера карт в диапазоне"""
    result = []
    for number in range(start, end + 1):
        card_str = str(number).zfill(16)
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        result.append(formatted)
    return result
