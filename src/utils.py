import json
import logging
from typing import List, Dict, Any


# Создаем логгер для модуля utils
utils_logger = logging.getLogger('utils')
utils_logger.setLevel(logging.DEBUG)

# Создаем файловый handler
file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)

# Добавляем handler к логгеру
utils_logger.addHandler(file_handler)


def read_json_file(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает JSON файл и возвращает список транзакций
    """
    utils_logger.debug(f"Попытка чтения файла: {filepath}")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if isinstance(data, list):
                utils_logger.info(f"Файл прочитан. Записей: {len(data)}")
                return data
            else:
                utils_logger.warning("Файл не содержит список данных")
                return []

    except FileNotFoundError:
        utils_logger.error("Файл не найден")
        return []
    except json.JSONDecodeError:
        utils_logger.error("Файл содержит некорректный JSON")
        return []
    except Exception as e:
        utils_logger.error(f"Ошибка при чтении: {str(e)}")
        return []
