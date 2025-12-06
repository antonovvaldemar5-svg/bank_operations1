from src.widget import get_date, mask_account_card


def test_mask_account_card_visa():
    """Маскировка Visa карты."""
    result = mask_account_card('Visa Platinum 7000792289606361')
    assert result == 'Visa Platinum 7000 79** **** 6361'


def test_mask_account_card_mastercard():
    """Маскировка MasterCard."""
    result = mask_account_card('MasterCard 7158300734726758')
    assert result == 'MasterCard 7158 30** **** 6758'


def test_mask_account_card_schet():
    """Маскировка счета."""
    result = mask_account_card('Счет 73654108430135874305')
    assert result == 'Счет **4305'


def test_get_date():
    """Форматирование даты."""
    result = get_date('2023-12-01T10:30:00.000')
    assert result == '01.12.2023'
