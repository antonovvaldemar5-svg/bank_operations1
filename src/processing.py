from typing import List, Dict, Any


def filter_by_state(
        operations: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует банковские операции по статусу.

    Берет список операций и оставляет только те,
    у которых статус совпадает с переданным значением.
    Если не указать статус, будет искать 'EXECUTED'.
    """
    result = []
    for operation in operations:
        if operation.get("state") == state:
            result.append(operation)
    return result


def sort_by_date(
        operations: List[Dict[str, Any]], reverse: bool = False
) -> List[Dict[str, Any]]:
    """
    Сортирует банковские операции по дате.

    Упорядочивает операции от старых к новым.
    Если передать reverse=True, будет от новых к старым.
    """
    sorted_operations = sorted(
        operations, key=lambda x: x.get("date", ""), reverse=reverse
    )
    return sorted_operations
