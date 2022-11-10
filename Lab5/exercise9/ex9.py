"""
Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs). The
function should return a list of dictionaries for each pair (in the same order as in the input list) that contain the
following keys (as strings): sum (the value should be sum of the 2 numbers), prod (the value should be product of the
two numbers), pow (the value should be the first number raised to the power of the second number)
"""


def list_of_tuples_to_dict(**kwargs):
    if len(kwargs.keys()) > 1 or "pairs" not in kwargs.keys():
        return "'pairs' parameter not found"

    returned_list = []
    for elements in kwargs['pairs']:
        current_dict = dict()
        current_dict['sum'] = elements[0] + elements[1]
        current_dict['prod'] = elements[0] * elements[1]
        current_dict['pow'] = elements[0] ** elements[1]
        returned_list.append(current_dict)

    return returned_list


if __name__ == '__main__':
    print(list_of_tuples_to_dict(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]))