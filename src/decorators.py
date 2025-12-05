def log(filename=None):
    """
    Декоратор для логирования работы функций.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)

                return result

            except Exception as e:
                msg = f"{func.__name__} error: {type(e).__name__}. "
                msg += f"Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg + "\n")
                else:
                    print(msg)

                raise

        return wrapper
    return decorator
