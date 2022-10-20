"""
    EX1: Write a function that receives as parameters two lists a and b and returns a list of sets containing:
    (a intersected with b, a reunited with b, a - b, b - a)
"""

def ex1(list_a: list, list_b: list):
    """"""
    a_intersected_b = set(list_a) & set(list_b)
    a_reunited_b = set(list_a) | set(list_b)
    a_minus_b = set(list_a) - set(list_b)
    b_minus_a = set(list_b) - set(list_a)
    response = [a_intersected_b, a_reunited_b, a_minus_b, b_minus_a]
    return response


print("EX1: ", ex1([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))


"""
    EX2: Write a function that receives a string as a parameter and returns a dictionary in which the keys are the 
    characters in the character string and the values are the number of occurrences of that character in the given text.
"""

def ex2(input_string: str):
    """"""
    letter_count = dict()
    for character in input_string:
        if letter_count.get(character) is None:
            letter_count[character] = 1
        else:
            letter_count[character] = (letter_count.get(character) + 1)
    return letter_count


print("EX2: ", ex2('Ana has apples.'))


"""
    EX3: Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries 
    must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
"""

def ex3(dict_a: dict, dict_b: dict):
    """"""
    if dict_a.keys() != dict_b.keys():
        return False
    for key in dict_a.keys():
        if type(dict_a[key]) == dict:
            if not ex3(dict_a[key], dict_b[key]):
                return False
        elif type(dict_a[key]) == list:
            if not ex3(dict_a[key], dict_b[key]):
                return False
        elif type(dict_a[key]) == set:
            if not ex3(dict_a[key], dict_b[key]):
                return False
        else:
            if dict_a[key] != dict_b[key]:
                return False
    return True





