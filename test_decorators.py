from decorators import hello, timer, retry

@hello
def say_hello():
    print("Привет")

@timer
def start_timer():
    return "hello"

@retry(attempts=2)
def retry_test():
    raise ValueError("сбой")

say_hello()
start_timer()
retry_test()