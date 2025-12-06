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


def test_log_error_to_console(capsys):
    """Тест логирования ошибки в консоль"""

    @log()
    def failing_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        failing_func()

    captured = capsys.readouterr()
    assert "failing_func error: ValueError" in captured.out


def test_log_with_kwargs():
    """Тест логирования функции с keyword-аргументами"""

    @log(filename="kwargs_test.txt")
    def greet(name, age=None):
        return f"Hello {name}, age {age}"

    result = greet("Vladimir", age=25)
    assert "Hello Vladimir, age 25" in result

    with open("kwargs_test.txt", "r", encoding="utf-8") as f:
        log_content = f.read()

    assert "greet ok" in log_content
    os.remove("kwargs_test.txt")


def test_log_no_args():
    """Тест логирования функции без аргументов"""

    @log()
    def get_version():
        return "1.0.0"

    result = get_version()
    assert result == "1.0.0"


def test_log_multiple_calls():
    """Тест множественных вызовов"""

    @log(filename="multi_test.txt")
    def counter():
        if not hasattr(counter, "count"):
            counter.count = 0
        counter.count += 1
        return counter.count

    counter()
    counter()
    result = counter()

    assert result == 3

    with open("multi_test.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) == 3
    assert all("counter ok" in line for line in lines)
    os.remove("multi_test.txt")


def test_log_with_different_exceptions():
    """Тест разных типов исключений"""

    @log(filename="exceptions_test.txt")
    def raise_custom_error():
        raise TypeError("Custom type error")

    with pytest.raises(TypeError):
        raise_custom_error()

    with open("exceptions_test.txt", "r", encoding="utf-8") as f:
        log_content = f.read()

    assert "raise_custom_error error: TypeError" in log_content
    os.remove("exceptions_test.txt")
