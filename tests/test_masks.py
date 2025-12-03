import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    """Тест маскировки номера карты"""
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"
    assert get_mask_card_number(9876543210987654) == "9876 54** **** 7654"


def test_get_mask_account():
    """Тест маскировки номера счета"""
    assert get_mask_account(12345678901234567890) == "**7890"
    assert get_mask_account(98765432101234560000) == "**0000"


def test_get_mask_card_number_string_input():
    """Тест маскировки карты со строковым вводом"""
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"


def test_get_mask_account_string_input():
    """Тест маскировки счета со строковым вводом"""
    assert get_mask_account("12345678901234567890") == "**7890"


def test_get_mask_card_number_short():
    """Тест маскировки короткого номера карты"""
    assert get_mask_card_number(1234) == "1234"


def test_get_mask_account_short():
    """Тест маскировки короткого номера счета"""
    assert get_mask_account(123) == "**123"