from typing import List, Dict, Any

def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """ Фильтрует список операций по статусу """
    result =[]
    for operation in operations:
        if operation.get("state") == state:
            result.append(operation)
        return result

    def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
        """ функция сортирует операции по дате """
        sorted_operations = sorted(operations, key=lambda  x: x.get("date", ""), reverse=reverse)
        return sorted_operations