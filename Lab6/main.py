"""
EX1: Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of
alphanumeric characters.
"""
import re
import xml.etree.ElementTree as ET


def extract_words(text):
    return re.findall('\w{1,}', text)


"""
EX2: Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns those 
long-length x substrings that match the regular expression.
"""


def extract_words_regex(regex, text, x):
    matches = []
    for sub in range(0, len(text) - x + 1):
        if re.match(regex + "{" + str(x) + "}", text[sub:sub + x]):
            matches.append(text[sub:sub + x])
    return matches


"""
EX3: Write a function that receives as a parameter a string of text characters and a list of regular expressions and 
returns a list of strings that match on at least one regular expression given as a parameter.
"""


def extract_words_regex_list(regex_list, text):
    matches = []
    for regex in regex_list:
        matches += re.findall(regex, text)
    return matches


"""
EX4: Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those 
elements that have as attributes all the keys in the dictionary and values the corresponding values. For 
example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags whose 
attributes are class="url" si name="url-form" si data-id="item".
"""


def extract_elements_by_attrs(xml_path, attrs):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return [elem.tag for elem in root.iter() if all([elem.attrib.get(key) == value for key, value in attrs.items()])]


"""
EX5: Write another variant of the function from the previous exercise that returns those elements that have at least one 
attribute that corresponds to a key-value pair in the dictionary.
"""


def extract_elements_by_attrs2(xml_path, attrs):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return [elem.tag for elem in root.iter() if any([elem.attrib.get(key) == value for key, value in attrs.items()])]


"""
EX6: Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship 
means replacing characters from odd positions with *.
"""


def censor_words(text):
    return re.sub(r'\b([aeiou])(.*?)([aeiou])\b', r'\1' + r'\2'.replace(r'\2', r'*' * (len(r'\2') - 1)) + r'\3', text)


"""
EX7: Verify using a regular expression whether a string is a valid CNP.
"""


def is_valid_cnp(cnp):
    return re.match(r'^[1-8]\d{2}((0[1-9])|(1[0-2]))((0[1-9])|([1-2]\d)|(3[0-1]))\d{4}$', cnp)


"""
EX8: Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression 
given as a parameter or contains a string that matches the same expression. Files that satisfy both conditions will be 
prefixed with ">>"
"""


def find_files(path, regex):
    import os
    for root, dirs, files in os.walk(path):
        for file in files:
            if re.match(regex, file):
                print('>>' + os.path.join(root, file))
            elif re.search(regex, file):
                print(os.path.join(root, file))


if __name__ == '__main__':
    print("EX1:", extract_words('Hello, world!'))
    print("EX2:", extract_words_regex('[a-zA-Z0-9]', 'Hello, world!', 4))
    print("EX3:", extract_words_regex_list(['\w+', '\d+'], 'Hello, world! 123'))
    print("EX4:", extract_elements_by_attrs('test.xml', {'seven': 'engine'}))
    print("EX5:", extract_elements_by_attrs2('test.xml', {'seven': 'engine', 'sky': 'happily'}))
    # print(censor_words('Hello, world!'))
    # print(is_valid_cnp('1234567890123'))
    # find_files('C:\\Users\\User\\Desktop\\', r'\w+')
