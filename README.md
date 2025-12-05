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
## Новый функционал: Чтение CSV и Excel файлов

### Функции:
- `read_csv_file(filepath)` - чтение транзакций из CSV
- `read_excel_file(filepath)` - чтение транзакций из Excel

### Пример использования:
```python
from src.file_reader import read_csv_file, read_excel_file

csv_transactions = read_csv_file('data/transactions.csv')
excel_transactions = read_excel_file('data/transactions_excel.xlsx')