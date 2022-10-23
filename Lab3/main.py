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
        elif type(dict_a[key]) == tuple or type(dict_a[key]) == set:
            if not ex3(dict.fromkeys(dict_a[key]), dict.fromkeys(dict_b[key])):
                return False
        else:
            if dict_a[key] != dict_b[key]:
                return False
    return True


print("EX4: ", ex3({'asda': {3, 4, 12}, 'ana': 2, 'ioana': (3, 1)}, {'asda': {56, 12, 111}, 'ana': 3, 'ioana': (3, 1)}))


"""
    EX4: The build_xml_element function receives the following parameters: tag, content, and key-value elements given 
    as name-parameters. Build and return a string that represents the corresponding XML element. Example: build_xml_element 
    ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns  the string = 
    "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
"""

def ex4(tag: str, content: str, **parameters):
    my_xml = '<'
    my_xml += tag + ' '
    for key in parameters:
        my_xml += key + ' =' + parameters[key] + ' '
    my_xml += '>' + content + '</' + tag + '>'
    return my_xml


print("EX4: ", ex4("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))


"""
    EX5: The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for 
    a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix", 
    "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at 
    the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the 
    rules, False otherwise.
"""

def validate_dict(rules: set, dictionary: dict):
    key_rules = []
    for rule in rules:
        key_rules.append(rule[0])

    for key in dictionary:
        if key not in key_rules:
            print(key)
            return False

    for key in dictionary:
        key_rule = [x for x in rules if x[0] == key]
        if not dictionary[key].startswith(key_rule[0][1]):
            return False
        if not dictionary[key].endswith(key_rule[0][3]):
            return False
        if dictionary[key].find(key_rule[0][2]) == -1 or \
           dictionary[key].find(key_rule[0][2]) == 0 or \
           dictionary[key].find(key_rule[0][2]) >= len(dictionary[key]) - len(key_rule[0][2]):
            return False

    return True


print("EX5: ", validate_dict({("key1", "", "inside", ""), ("key2", "", "valid", "")},
                             {"key1": "come inside, it's too cold out", "key2": "this is not valid"}))


"""
    EX6: Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of 
    unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve 
    this objective).
"""

def ex6(input_list: list):
    return len(input_list) - 2 * (len(input_list) - len(set(input_list))), len(input_list) - len(set(input_list))


print("EX6: ", ex6(['ioana', 'maria', 'cristina', 'maria', 'cristina']))


"""
    EX7: Write a function that receives a variable number of sets and returns a dictionary with the following operations 
    from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a 
    and b are two sets, and op is the applied operator: |, &, -. 
"""

def ex7(*input_sets: set):
    output_dict = dict([])
    for i in range(0, len(input_sets)):
        j = i + 1
        while j < len(input_sets):
            output_dict[str(input_sets[i]) + " | " + str(input_sets[j])] = input_sets[i] | input_sets[j]
            output_dict[str(input_sets[i]) + " & " + str(input_sets[j])] = input_sets[i] & input_sets[j]
            output_dict[str(input_sets[i]) + " - " + str(input_sets[j])] = input_sets[i] - input_sets[j]
            output_dict[str(input_sets[j]) + " - " + str(input_sets[i])] = input_sets[j] - input_sets[i]
            j += 1
    return output_dict


print("EX7: ", ex7({1, 2}, {2, 3}))


"""
    EX8: Write a function that receives a single dict parameter named mapping. This dictionary always contains a string 
    key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the 
    following way: the value of the current key is the key for the next value, until you find a loop (a key that was 
    visited before). The function must return the list of objects obtained as previously described.
"""

def ex8(mapping: dict):
    my_loop = []
    if 'start' not in mapping.keys():
        return "'start' key not found!"

    next_key = mapping.get('start')
    my_loop.append(next_key)
    while True:
        if mapping.get(next_key) is None:
            return 'No loop found!'
        if mapping.get(next_key) in my_loop:
            return my_loop
        next_key = mapping.get(next_key)
        my_loop.append(next_key)


print("EX8: ", ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


"""
    EX9: Write a function that receives a variable number of positional arguments and a variable number of keyword 
    arguments adn will return the number of positional arguments whose values can be found among keyword arguments 
    values.
"""

def ex9(*pos_arg, **keyword_arg):
    counter = 0
    for value in pos_arg:
        if value in keyword_arg.values():
            counter += 1
    return counter


print("EX9: ", ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))