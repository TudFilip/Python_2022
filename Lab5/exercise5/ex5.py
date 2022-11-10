"""
Write a function with one parameter which represents a list. The function will return a new list containing all the
numbers found in the given list.
"""
import numbers


def list_of_numbers_from_given_list(input_list: list):
    return [element for element in input_list if isinstance(element, numbers.Number)]


if __name__ == '__main__':
    print(list_of_numbers_from_given_list([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
    