from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file_success():
    """Тест успешного чтения JSON"""
    mock_data = '[{"id": 1, "amount": 100}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json_file("dummy.json")
        assert len(result) == 1
        assert result[0]["id"] == 1


def test_read_json_file_not_found():
    """Тест когда файл не найден"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json_file("nonexistent.json")
        assert result == []


def test_read_json_file_invalid_json():
    """Тест некорректного JSON"""
    mock_data = "{invalid json"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json_file("invalid.json")
        assert result == []


def test_read_json_file_not_list():
    """Тест когда JSON не список"""
    mock_data = '{"id": 1, "amount": 100}'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json_file("not_list.json")
        assert result == []
