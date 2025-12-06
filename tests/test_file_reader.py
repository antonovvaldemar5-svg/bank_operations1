import os
from unittest.mock import MagicMock, patch

from src.file_reader import read_csv_file, read_excel_file


def setup_module():
    """Создает папку logs перед тестами"""
    os.makedirs("logs", exist_ok=True)


def test_read_csv_file_success():
    """Тест успешного чтения CSV"""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]

    with patch("pandas.read_csv", return_value=mock_df):
        result = read_csv_file("test.csv")
        assert len(result) == 1
        assert result[0]["id"] == 1


def test_read_excel_file_success():
    """Тест успешного чтения Excel"""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 2, "amount": 200}]

    with patch("pandas.read_excel", return_value=mock_df):
        result = read_excel_file("test.xlsx")
        assert len(result) == 1
        assert result[0]["id"] == 2


def test_read_csv_file_not_found():
    """Тест когда CSV файл не найден"""
    with patch("pandas.read_csv", side_effect=FileNotFoundError):
        result = read_csv_file("nonexistent.csv")
        assert result == []


def test_read_excel_file_not_found():
    """Тест когда Excel файл не найден"""
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = read_excel_file("nonexistent.xlsx")
        assert result == []


def test_read_csv_file_general_error():
    """Тест общей ошибки при чтении CSV"""
    with patch("pandas.read_csv", side_effect=Exception("Test error")):
        result = read_csv_file("error.csv")
        assert result == []


def test_read_excel_file_general_error():
    """Тест общей ошибки при чтении Excel"""
    with patch("pandas.read_excel", side_effect=Exception("Test error")):
        result = read_excel_file("error.xlsx")
        assert result == []
