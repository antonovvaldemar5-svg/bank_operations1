"""" Модуль виджета для обработки банковских операций """

from .masks import get_mask_card_number, get_mask_account


def mask_account_card(card_info: str) -> str:
    """ Маскирует номер карты или счета в зависимости от типа """


# Определяем тип (карта или счет)
    if "Счет" in card_info:
        # Обработка счета
        parts = card_info.split()
        if len(parts) < 2:
            return card_info

        account_number_str = parts[-1]
        try:
            account_number = int(account_number_str)
            masked_account = get_mask_account(account_number)
            return f"Счет {masked_account}"
        except ValueError:
            return card_info
    else:
# Обработка карты
        parts = card_info.split()
        if len(parts) < 2:
            return card_info

        card_number_str = parts[-1]
        card_name = " ".join(parts[:-1])

        try:
            card_number = int(card_number_str)
            masked_card = get_mask_card_number(card_number)
            return f"{card_name} {masked_card}"
        except ValueError:
            return card_info


def get_date(date_string: str) -> str:
    """ Преобразует строку с датой в формат ДД.ММ.ГГГГ """
    # Разделяем дату и время
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
