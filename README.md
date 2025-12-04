### Модуль decorators

#### Декоратор log
Логирует выполнение функций в файл или консоль:

```python
from src.decorators import log

# Логирование в файл
@log(filename="operations.log")
def process_transaction(amount, currency):
    return f"Processed {amount} {currency}"

process_transaction(100, "USD")

# Логирование в консоль
@log()
def validate_card(card_number):
    return len(str(card_number)) == 16

validate_card(1234567812345678)