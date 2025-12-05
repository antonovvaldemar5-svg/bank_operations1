import pandas as pd
from typing import List, Dict, Any
import logging

# Логгер для модуля
file_reader_logger = logging.getLogger('file_reader')
file_reader_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/file_reader.log', mode='w')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
file_reader_logger.addHandler(file_handler)


def read_csv_file(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает CSV файл и возвращает список транзакций
    """
    file_reader_logger.debug(f"Чтение CSV файла: {filepath}")

    try:
        df = pd.read_csv(filepath, encoding='utf-8')
        transactions = df.to_dict('records')
        file_reader_logger.info(
            f"CSV файл прочитан. Записей: {len(transactions)}"
        )
        return transactions
    except FileNotFoundError:
        file_reader_logger.error(f"CSV файл не найден: {filepath}")
        return []
    except Exception as e:
        file_reader_logger.error(f"Ошибка чтения CSV: {str(e)}")
        return []


def read_excel_file(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает Excel файл и возвращает список транзакций
    """
    file_reader_logger.debug(f"Чтение Excel файла: {filepath}")

    try:
        df = pd.read_excel(filepath)
        transactions = df.to_dict('records')
        file_reader_logger.info(
            f"Excel файл прочитан. Записей: {len(transactions)}"
        )
        return transactions
    except FileNotFoundError:
        file_reader_logger.error(f"Excel файл не найден: {filepath}")
        return []
    except Exception as e:
        file_reader_logger.error(f"Ошибка чтения Excel: {str(e)}")
        return []
