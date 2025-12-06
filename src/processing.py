from datetime import datetime, timezone
from typing import Any, Dict, List


def filter_by_state(
    transactions: List[Dict[str, Any]],
    state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по статусу
    """
    return [
        transaction for transaction in transactions
        if transaction.get("state") == state
    ]


def sort_by_date(
    transactions: List[Dict[str, Any]],
    reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует транзакции по дате
    """

    def parse_date(date_str: str) -> datetime:
        if date_str.endswith('Z'):
            date_str = date_str[:-1] + '+00:00'

        dt = datetime.fromisoformat(date_str)

        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)

        return dt

    return sorted(
        transactions,
        key=lambda x: parse_date(x["date"]),
        reverse=reverse
    )
