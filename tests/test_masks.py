# Тесты для tests
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Тест маскировки номера карты"""
    result = get_mask_card_number(1234567890123456)
    expected = "1234 56** **** 3456"
    print(f"Тест карты: {result} == {expected}")

    # Проверяем другой номер карты
    result2 = get_mask_card_number(5555444433331111)
    expected2 = "5555 44** **** 1111"
    print(f"Тест карты 2: {result2} == {expected2}")


def test_get_mask_account() -> None:
    # Проверяем обычный номер счета
    result = get_mask_account(1234567890)
    expected = "**7890"
    print(f"Тест счета: {result} == {expected}")

    # Проверяем короткий номер счета
    result2 = get_mask_account(1234)
    expected2 = "**1234"
    print(f"Тест короткого счета: {result2} == {expected2}")

    # Проверяем длинный номер счета
    result3 = get_mask_account(112233445566)
    expected3 = "**5566"
    print(f"Тест длинного счета: {result3} == {expected3}")


# Запускаем тесты при прямом выполнении файла
if __name__ == "__main__":
    test_get_mask_card_number()
    test_get_mask_account()
    print("Все тесты завершены!")
