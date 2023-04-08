

def my_logger(original_function):
    import logging
    logging.basicConfig(filename=f"{original_function.__name__}", level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args}, and kwargs: {kwargs}"
        )
        return original_function(*args, **kwargs)
    return wrapper


@my_logger
def display_user_info(name, age):
    print(f"username: {name}, age: {age}")


display_user_info("srinu", 22)
display_user_info("pavan", 23)