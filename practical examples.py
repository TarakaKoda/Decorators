import time
from functools import wraps


def my_logger(original_function):
    import logging
    logging.basicConfig(filename=f"{original_function.__name__}", level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args}, and kwargs: {kwargs}"
        )
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{original_function.__name__} ran in: {t2}")
        return result

    return wrapper


@my_logger
@my_timer
def display_user_info(name, age):
    time.sleep(1)
    print(f"username: {name}, age: {age}")


display_user_info("pavan", 22)

