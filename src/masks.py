def get_mask_card_number(card_number):
    """Маскирует карту"""
    card_str = str(card_number)
    if len(card_str) != 16:
        return str(card_number)
    first_six = card_str[:6]
    last_four = card_str[-4:]
    formatted_first = f"{first_six[:4]} {first_six[4:6]}"
    masked_middle = "** ****"
    return f"{formatted_first}{masked_middle} {last_four}"


def get_mask_account(account_number):
    """Маскирует счет"""
    account_str = str(account_number)
    if len(account_str) < 4:
        return f"**{account_str}"
    last_four = account_str[-4:]
    return f"**{last_four}"
