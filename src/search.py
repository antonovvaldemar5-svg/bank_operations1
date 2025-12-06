import re
from collections import Counter
from typing import Any, Dict, List


def search_by_description(
    transactions: List[Dict[str, Any]],
    search_string: str
) -> List[Dict[str, Any]]:
    """Ищет транзакции по строке в описании."""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [
        t for t in transactions
        if pattern.search(t.get('description', ''))
    ]


def count_by_categories(
    transactions: List[Dict[str, Any]],
    categories: List[str]
) -> Dict[str, int]:
    """Считает количество операций по категориям."""
    counter = Counter()
    for t in transactions:
        desc = t.get('description', '').lower()
        for cat in categories:
            if cat.lower() in desc:
                counter[cat] += 1
    return dict(counter)
