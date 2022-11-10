"""
Write a function that receives a list with integers as parameter that contains an equal number of even and odd numbers
that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers (Xi, Yi)
such that Xi is the i-th even number in the list and Yi is the i-th odd number
"""


def order_even_and_odd_numbers(input_list: list):
    return list(zip([xi for xi in input_list if xi % 2 == 0], [yi for yi in input_list if yi % 2 != 0]))


if __name__ == '__main__':
    print(order_even_and_odd_numbers([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))