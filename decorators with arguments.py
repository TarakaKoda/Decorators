def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, f"this the is statement before the {original_function.__name__} execution")
            result = original_function(*args, **kwargs)
            print(prefix, f"this is after the execution of the {original_function.__name__}\n")
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator("TESING: ")
def display_info(name,age):
    print(f"username: {name}, age: {age}")


@prefix_decorator("LOG: ")
def about_page():
    print("this is our about page")


display_info("srinu", 22)
display_info("pavan", 23)
about_page()