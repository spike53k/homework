from functools import wraps
import time

def hello(func):
    def wrapper(*args, **kwargs):
        print("Начинаем")
        result = func(*args, **kwargs)
        print("Готово")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        all_time = end - start
        print(f"Время выполнения: {all_time:.4f}")
        return result
    return wrapper

def retry(attempts=3, delay=0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == attempts - 1:
                        raise RuntimeError(f"Ошибка {e}") from e
        return wrapper
    return decorator