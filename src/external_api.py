import os
import requests
from typing import Dict
from dotenv import load_dotenv  # ← ДОБАВЬ ЭТО

# Загружаем переменные из .env
load_dotenv()  # ← И ЭТО


def convert_to_rubles(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли
    """
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount

    if currency in ['USD', 'EUR']:
        api_key = os.getenv('EXCHANGE_API_KEY')  # ← теперь возьмет из .env
        if not api_key:
            return amount

        url = "https://api.apilayer.com/exchangerates_data/convert"
        params = {
            'to': 'RUB',
            'from': currency,
            'amount': amount
        }
        headers = {'apikey': api_key}

        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json()['result']
        except requests.RequestException:
            pass

    return amount