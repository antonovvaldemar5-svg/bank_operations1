from .masks import get_mask_card_number, get_mask_account


def mask_account_card(card_info):
    """Маскирует карту или счет"""
    if not card_info:  # Добавляем проверку на пустую строку
        return ""

    if "Счет" in card_info:
        parts = card_info.split()
        if len(parts) < 2:  # Проверяем что есть номер счета
            return card_info
        account_number = parts[-1]
        try:
            masked = get_mask_account(int(account_number))
            return f"Счет {masked}"
        except ValueError:
            return card_info
    else:
        parts = card_info.split()
        if len(parts) < 2:  # Проверяем что есть номер карты
            return card_info
        card_number = parts[-1]
        card_name = " ".join(parts[:-1])
        try:
            masked = get_mask_card_number(int(card_number))
            return f"{card_name} {masked}"
        except ValueError:
            return card_info


def get_date(date_string):
    """Конвертирует дату"""
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"