def filter_by_state(operations, state="EXECUTED"):
    """Фильтрует по статусу"""
    result = []
    for operation in operations:
        if operation.get("state") == state:
            result.append(operation)
    return result


def sort_by_date(operations, reverse=True):
    """Сортирует по дате"""
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
