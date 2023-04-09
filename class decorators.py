class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"call method executes this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)

    # we can add more functionality even after execution of our original function.
    # def __call__(self, *args, **kwargs):
    #     print(f"call method executes this before {self.original_function.__name__}")
    #     self.original_function(*args, **kwargs)
    #     print("this is after original function execution")
    #     return self.original_function(*args, **kwargs)


@decorator_class
def display(name,age):
    print(f"name: {name}, age: {age}")


@decorator_class
def display_about():
    print("this is our about page")


display("srinu",22)
display_about()