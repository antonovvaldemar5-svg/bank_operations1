from src.widget import mask_account_card, get_date
import pytest


# ПАРАМЕТРИЗАЦИЯ для маскировки карт
@pytest.mark.parametrize("card_info, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card_parametrized(card_info, expected):
    """Тестирует маскировку разных типов карт и счетов"""
    result = mask_account_card(card_info)
    assert result == expected


# ПАРАМЕТРИЗАЦИЯ для дат
@pytest.mark.parametrize("date_string, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ("2024-01-01T00:00:00.000000", "01.01.2024"),
])
def test_get_date_parametrized(date_string, expected):
    """Тестирует преобразование разных дат"""
    result = get_date(date_string)
    assert result == expected

    def test_mask_account_card_empty():
        """Тест пустой строки"""
        result = mask_account_card("")
        assert result == ""

    def test_mask_account_card_only_spaces():
        """Тест строки с пробелами"""
        result = mask_account_card("   ")
        assert result == "   "

    def test_mask_account_card_invalid_number():
        """Тест карты с буквами в номере"""
        result = mask_account_card("Visa ABCDEFGHIJKLMNOP")
        assert result == "Visa ABCDEFGHIJKLMNOP"

    def test_get_date_empty_string():
        """Тест пустой даты"""
        result = get_date("")
        assert result == ""

    def test_get_date_invalid_format():
        """Тест неверного формата даты"""
        result = get_date("invalid-date")
        assert "invalid-date" in result