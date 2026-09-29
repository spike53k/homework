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