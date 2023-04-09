# number = 9
# if all([number%i != 0 for i in range(2,number)]):
#     print(f"{number} is a prime number")
# else:
#     print(f"{number} is not a prime number")

# def true_or_false(number):
#     return True if number%2 ==0 else False
#
# print(true_or_false(5))
import time
from functools import wraps


def repeat(num_repeat=1):
    def decorator_function(original_function):
        @wraps(original_function)
        def wrapper_function(*args, **kwargs):
            result = None
            for i in range(num_repeat):
                result = original_function(*args, **kwargs)
            return result

        return wrapper_function

    return decorator_function


def timmer(repeat=1):
    def decorator_function(original_function):
        @wraps(original_function)
        def wrapper_function(*args, **kwargs):
            total_time = 0
            result = None
            for i in range(repeat):
                starting_time = time.time()
                result = original_function(*args, **kwargs)
                end_time = time.time() - starting_time
                total_time += end_time
            average_time = total_time / repeat
            print(f"{original_function.__name__} has taken {average_time:.6f} seconds on average run")
            return result

        return wrapper_function

    return decorator_function


@timmer(repeat=5)
def square(number):
    yield [x * x for x in number]


@timmer(repeat=2)
@repeat(num_repeat=2)
def display_name(name, age):
    time.sleep(1)
    print(f"username: {name}, age: {age}")


number = range(1, 10)
result = square(number)
total = 0
print(result.__name__)
for i in result:
    for num in i:
        total += num
print(f"sum of all squared numbers: {total}")

display_name("srinu", 22)
