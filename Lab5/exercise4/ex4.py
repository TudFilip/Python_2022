"""
Write a function that receives a variable number of arguments and keyword arguments. The function returns a list
containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with
minimum 3 characters.
"""


def specific_dictionaries_given_as_parameters(*args, **kwargs):
    dict_found = []
    for parameter in args:
        if type(parameter) is dict and len(parameter.keys()) >= 2:
            for key in parameter.keys():
                if type(key) is str and len(key) >= 3:
                    dict_found.append(parameter)
                    break

    for parameter in kwargs.values():
        if type(parameter) is dict and len(parameter.keys()) >= 2:
            for key in parameter.keys():
                if type(key) is str and len(key) >= 3:
                    dict_found.append(parameter)
                    break

    return dict_found


if __name__ == '__main__':
    print(specific_dictionaries_given_as_parameters({1: 2, 3: 4, 5: 6},
                                                    {'a': 5, 'b': 7, 'c': 'e'},
                                                    {2: 3},
                                                    [1, 2, 3],
                                                    {'abc': 4, 'def': 5},
                                                    3764,
                                                    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
                                                    test={1: 1, 'test': True}
                                                    ))
