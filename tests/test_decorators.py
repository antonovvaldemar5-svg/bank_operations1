import os
import pytest
from src.decorators import log


def test_log_to_file():
    """Тест логирования в файл"""

    @log(filename="test_log.txt")
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5

    with open("test_log.txt", "r", encoding="utf-8") as f:
        log_content = f.read()

    assert "add ok" in log_content
    os.remove("test_log.txt")


def test_log_to_console(capsys):
    """Тест логирования в консоль"""

    @log()
    def multiply(x, y):
        return x * y

    result = multiply(4, 5)
    assert result == 20

    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_log_error_to_file():
    """Тест логирования ошибки в файл"""

    @log(filename="error_log.txt")
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    with open("error_log.txt", "r", encoding="utf-8") as f:
        log_content = f.read()

    assert "divide error: ZeroDivisionError" in log_content
    os.remove("error_log.txt")