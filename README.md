# Bank Operations Widget

Проект для работы с банковскими операциями.

## Использование

### Генераторы данных
```python
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Фильтрация транзакций по валюте USD
transactions = [
    {
        "operationAmount": {
            "amount": "100", 
            "currency": {"code": "USD"}
        },
        "description": "Перевод"
    }
]
usd_transactions = filter_by_currency(transactions, "USD")

# Получение описаний транзакций
descriptions = transaction_descriptions(transactions)

# Генерация номеров карт
for card in card_number_generator(1, 5):
    print(card)