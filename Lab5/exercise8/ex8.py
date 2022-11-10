"""
a) Write a function called print_arguments with one parameter named function. The function will return one new function
which prints the arguments and the keyword arguments received and will return the output of the function receives as a
parameter.
"""


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def f(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)

    return f


"""
b) Write a function called multiply_output with one parameter named function. The function will return one new function 
which returns the output of the function received multiplied by 2.
"""


def multiply_output(function):
    def f(*args, **kwargs):
        return function(*args, **kwargs) * 2
    return f


def multiply_by_three(x: int):
    return x * 3


"""
c) Write a function called augment_function with two parameters named function and decorators. decorators will be a list 
of functions which will have the same signature as the previous functions (print_arguments, multiply_output). 
augment_function will create a new function which is augmented using all the functions in the decorators list.
"""


def augment_function(function, decorators):
    def f(*args, **kwargs):
        result = function
        for deco in decorators:
            result = deco(result)
        return result(*args, **kwargs)

    return f


if __name__ == '__main__':
    print("EX 8, a:")
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)
    print(x)
    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)
    print(x)

    print("EX 8, b:")
    augmented_multiply_by_three = multiply_output(multiply_by_three)
    x = augmented_multiply_by_three(10)
    print(x)

    print("EX 8, c:")
    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
    x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4
    print(x)



