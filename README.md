# Bank Operations Widget

## Использование
```python
from src.generators import filter_by_currency, card_number_generator

# Пример
for card in card_number_generator(1, 3):
    print(card)

5. **Сохрани**

**Потом:**
```bash
git add src/generators.py tests/test_generators.py README.md
git commit -m "feat: add generators"
git push origin feature/generators