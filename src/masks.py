# Модуль для маскировки номера карты
def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер карты по принципу: ХХХХ ХХ** **** ХХХХ"""
    card_str = str(card_number)
    if len(card_str) != 16:
        return str(card_number)

    first_six = card_str[:6]  # первые 6 цифр
    last_four = card_str[-4:]  # последние 4 цифры
    formated_first = f"{first_six[4]} {first_six[4:6]}"
    masked_middle = "** ****"

    # Форматируем номер карты
    formated_first = f"{first_six[:4]} {first_six[4:6]}"
    masked_middle = "** ****"
    return f"{formated_first}{masked_middle} {last_four}"


def get_mask_account(account_number: int) -> str:
    """ Маскирует номер счета по принципу: **ХХХХ """
    account_str = str(account_number)

    if len(account_str) < 4:
        return f"**{account_str}"

    last_four = account_str[-4:]
    return f"**{last_four}"
