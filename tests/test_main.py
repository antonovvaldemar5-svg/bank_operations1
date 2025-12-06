from unittest.mock import patch

from src.main import main


def test_main_exit_on_wrong_choice():
    """Тест выхода при неверном выборе."""
    with patch('builtins.input', return_value='4'):
        with patch('builtins.print') as mock_print:
            main()
            # Проверяем что программа выводит сообщение о неверном выборе
            calls = [call[0][0] for call in mock_print.call_args_list]
            assert "Неверный выбор. Завершение программы." in str(calls)


def test_main_json_file_selection():
    """Тест выбора JSON файла."""
    with patch('builtins.input', side_effect=['1', 'EXECUTED', 'нет', 'нет']):
        with patch('src.main.read_json_file') as mock_read:
            with patch('src.main.filter_by_state') as mock_filter:
                with patch('src.main.print'):
                    mock_read.return_value = []
                    mock_filter.return_value = []
                    main()
                    # Проверяем что read_json_file вызывался
                    assert mock_read.called


def test_main_no_transactions():
    """Тест случая когда нет транзакций."""
    with patch('builtins.input', side_effect=['1', 'EXECUTED', 'нет', 'нет']):
        with patch('src.main.read_json_file', return_value=[]):
            with patch('src.main.filter_by_state', return_value=[]):
                with patch('builtins.print') as mock_print:
                    main()
                    # Ищем вывод о пустой выборке
                    output = "\n".join(
                        str(call[0][0]) for call in mock_print.call_args_list
                    )
                    assert "Не найдено ни одной транзакции" in output
