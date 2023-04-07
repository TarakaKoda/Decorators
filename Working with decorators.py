# Decorators
# "Decorators in python are special syntax for wrapping or modifying function or classes. They  allow you
# to add extra functionality to function or class, without changing their source code.
# @ followed by the decorated name

# To understand decorators you must have the knowledge of:
# First-class functions
# Closures
# here are some examples of first-class functions and closures

def outer_function():
    message = "h1"

    def inner_function():
        print(message)

    return inner_function


my_function = outer_function()


# my_function()
# my_function()
# my_function()


def outerfunction(msg):
    def innerfunction(name):
        print(f"{msg}, {name}")

    return innerfunction


#
# hi_function = outerfunction("hi")
# hello_function = outerfunction("hello")
#
# hi_function("pavan")
# hello_function("srinu")

# basic example of decorators
def first_function(original_function):
    def second_function(mg,msg):
        print(f"this is executed above the original function. {mg}")
        original_function(msg)
        print("after the original function")
        return original_function

    return second_function


@first_function
def add(msg):
    print(msg)


message = add("pavan", "srinu")
message("naruto")


