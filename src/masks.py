import logging


# Создаем логгер для модуля masks
masks_logger = logging.getLogger('masks')
masks_logger.setLevel(logging.DEBUG)

# Создаем файловый handler
file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)

# Добавляем handler к логгеру
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number):
    """Маскирует карту"""
    masks_logger.debug(f"Маскировка номера карты: {card_number}")

    try:
        card_str = str(card_number)
        if len(card_str) != 16:
            masks_logger.warning(f"Некорректная длина: {len(card_str)}")
            return str(card_number)

        result = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        masks_logger.info(f"Карта замаскирована: {result}")
        return result

    except Exception as e:
        masks_logger.error(f"Ошибка при маскировке: {str(e)}")
        return str(card_number)


def get_mask_account(account_number):
    """Маскирует счет"""
    masks_logger.debug(f"Маскировка номера счета: {account_number}")

    try:
        account_str = str(account_number)
        if len(account_str) < 4:
            masks_logger.warning(f"Слишком короткий: {len(account_str)}")
            return f"**{account_str}"

        result = f"**{account_str[-4:]}"
        masks_logger.info(f"Счет замаскирован: {result}")
        return result

    except Exception as e:
        masks_logger.error(f"Ошибка при маскировке: {str(e)}")
        return str(account_number)
