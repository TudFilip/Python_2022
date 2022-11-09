"""
Create a function and an anonymous function that receive a variable number of arguments. Both will return the sum of the
values of the keyword arguments.
"""


def sum_of_kwargs(*args, **kwargs):
    return sum(kwargs.values())


anon_sum_of_kwargs = lambda *args, **kwargs: sum(kwargs.values())

print(sum_of_kwargs(1, 2, c=3, d=4, e=5))
print(anon_sum_of_kwargs(1, 2, c=3, d=4, e=5))
