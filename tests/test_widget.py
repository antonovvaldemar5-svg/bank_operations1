from src.widget import mask_account_card


def test_mask_account_card_with_invalid_account():
    """Тест маскировки счета с нечисловым номером"""
    # Счет с буквами вместо цифр
    assert mask_account_card("Счет abcdef") == "Счет abcdef"
    # Счет с символами
    assert mask_account_card("Счет 12-34-56") == "Счет 12-34-56"


def test_mask_account_card_with_invalid_card():
    """Тест маскировки карты с нечисловым номером"""
    # Карта с буквами вместо цифр
    assert mask_account_card("Visa abcdef") == "Visa abcdef"
    # Карта с символами
    assert mask_account_card("MasterCard 12-34-56") == "MasterCard 12-34-56"


def test_mask_account_card_only_account_word():
    """Тест когда только слово 'Счет' без номера"""
    assert mask_account_card("Счет") == "Счет"


def test_mask_account_card_only_card_name():
    """Тест когда только название карты без номера"""
    assert mask_account_card("Visa") == "Visa"
