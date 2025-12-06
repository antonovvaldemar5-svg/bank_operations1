from src.search import count_by_categories, search_by_description


def test_search_by_description():
    trans = [
        {'description': 'Перевод организации'},
        {'description': 'Оплата услуг'},
        {'description': 'Перевод между счетами'}
    ]

    result = search_by_description(trans, 'перевод')
    assert len(result) == 2
    assert all('перевод' in t['description'].lower() for t in result)


def test_count_by_categories():
    trans = [
        {'description': 'Перевод организации'},
        {'description': 'Оплата услуг'},
        {'description': 'Перевод между счетами'},
        {'description': 'Оплата интернета'}
    ]

    result = count_by_categories(trans, ['Перевод', 'Оплата'])
    assert result == {'Перевод': 2, 'Оплата': 2}
