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


def test_search_special_characters():
    """Поиск с специальными символами."""
    trans = [{'description': 'Оплата [специальная]'}]
    result = search_by_description(trans, '[специальная]')
    assert len(result) == 1


def test_search_partial_word():
    """Поиск части слова."""
    trans = [{'description': 'Перевод организации'}]
    result = search_by_description(trans, 'перев')
    assert len(result) == 1


def test_count_multiple_categories():
    """Подсчет когда транзакция попадает в несколько категорий."""
    trans = [{'description': 'Перевод и оплата'}]
    result = count_by_categories(trans, ['Перевод', 'Оплата'])
    assert result['Перевод'] == 1
    assert result['Оплата'] == 1


def test_search_empty_string():
    """Поиск с пустой строкой."""
    trans = [{'description': 'Перевод'}]
    result = search_by_description(trans, '')
    assert len(result) == 1


def test_count_case_sensitive():
    """Подсчет с разным регистром."""
    trans = [{'description': 'Перевод'}, {'description': 'перевод'}]
    result = count_by_categories(trans, ['Перевод'])
    assert result == {'Перевод': 2}


def test_search_none_description():
    """Поиск когда description равен None."""
    trans = [{'description': None}, {'description': 'Перевод'}]
    result = search_by_description(trans, 'Перевод')
    assert len(result) == 1


def test_count_empty_transactions():
    """Подсчет с пустым списком транзакций."""
    result = count_by_categories([], ['Перевод'])
    assert result == {}
