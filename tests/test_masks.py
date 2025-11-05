from src.masks import get_mask_card_number, get_mask_account
import pytest


# ФИКСТУРА для тестовых номеров карт
@pytest.fixture
def sample_cards():
    return [7000792289606361, 1596837868705199, 12345]


# ФИКСТУРА для тестовых номеров счетов
@pytest.fixture
def sample_accounts():
    return [73654108430135874305, 64686473678894779589, 123]


# ПАРАМЕТРИЗАЦИЯ для карт
@pytest.mark.parametrize("card_number, expected", [
    (7000792289606361, "7000 79** **** 6361"),
    (1596837868705199, "1596 83** **** 5199"),
])
def test_get_mask_card_number_parametrized(card_number, expected):
    """Тестирует маскировку разных номеров карт"""
    result = get_mask_card_number(card_number)
    assert result == expected


# ПАРАМЕТРИЗАЦИЯ для счетов
@pytest.mark.parametrize("account_number, expected", [
    (73654108430135874305, "**4305"),
    (64686473678894779589, "**9589"),
    (123, "**123"),
])
def test_get_mask_account_parametrized(account_number, expected):
    """Тестирует маскировку разных номеров счетов"""
    result = get_mask_account(account_number)
    assert result == expected


def test_get_mask_card_number_invalid(sample_cards):
    """Тестирует невалидный номер карты используя фикстуру"""
    result = get_mask_card_number(sample_cards[2])  # 12345
    assert result == "12345"