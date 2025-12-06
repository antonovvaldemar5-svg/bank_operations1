import os
import requests
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rubles(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли
    """
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount

    if currency in ['USD', 'EUR']:
        api_key = os.getenv('EXCHANGE_API_KEY')
        if not api_key:
            return amount

        params = {
            'to': 'RUB',
            'from': currency,
            'amount': amount
        }
        headers = {'apikey': api_key}

        try:
            response = requests.get(
                EXCHANGE_API_URL,
                params=params,
                headers=headers,
                timeout=10
            )
            if response.status_code == 200:
                return response.json()['result']
        except requests.RequestException:
            pass

    return amount
