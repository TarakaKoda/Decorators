def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        if args:
            print(f"wrapper function before execution {args[0]}")
        else:
            print(f"wrapper function before execution")
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display_homepage():
    print("welcome to the home page\n")


@decorator_function
def display_user_details(name,age):
    print(f"username: {name}\nage: {age}\n")


display_homepage()
display_user_details("srinu",23)

# class decorator

