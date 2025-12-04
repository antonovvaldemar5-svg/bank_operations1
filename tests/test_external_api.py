from unittest.mock import patch, Mock
from src.external_api import convert_to_rubles


def test_convert_to_rubles_rub():
    """Тест когда транзакция уже в рублях"""
    transaction = {
        'operationAmount': {
            'amount': '1000.50',
            'currency': {'code': 'RUB'}
        }
    }
    result = convert_to_rubles(transaction)
    assert result == 1000.50


def test_convert_to_rubles_usd_with_mock():
    """Тест конвертации USD с моком API"""
    transaction = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'USD'}
        }
    }

    with patch('os.getenv', return_value='fake_api_key'):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': 7500.0}

        with patch('requests.get', return_value=mock_response):
            result = convert_to_rubles(transaction)
            assert result == 7500.0


def test_convert_to_rubles_no_api_key():
    """Тест когда нет API ключа"""
    transaction = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'USD'}
        }
    }

    with patch('os.getenv', return_value=None):
        result = convert_to_rubles(transaction)
        assert result == 100.0


def test_convert_to_rubles_api_error():
    """Тест ошибки API"""
    transaction = {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'USD'}
        }
    }

    with patch('os.getenv', return_value='fake_api_key'):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = 'Internal Server Error'

        with patch('requests.get', return_value=mock_response):
            result = convert_to_rubles(transaction)
            assert result == 100.0
