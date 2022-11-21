"""
EX1: Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of
alphanumeric characters.
"""
import re
import xml.etree.ElementTree as ET
import os


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
    all_matches = re.findall('[aeiouAEIOU]\w*[aeiouAEIOU]', text)
    censured_matches = []
    for match in all_matches:
        tmp = ''
        for i in range(1, len(match)+1):
            if i % 2 == 0:
                tmp += match[i-1]
            else:
                tmp += '*'
        censured_matches.append(tmp)

    return re.sub('[aeiouAEIOU]\w*[aeiouAEIOU]', lambda x: censured_matches.pop(0), text)


"""
EX7: Verify using a regular expression whether a string is a valid CNP.
"""


def is_valid_cnp(cnp):
    if re.match('^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$', cnp):
        return True
    return False


"""
EX8: Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression 
given as a parameter or contains a string that matches the same expression. Files that satisfy both conditions will be 
prefixed with ">>"
"""


def find_files(path, regex):
    for (root, directories, files) in os.walk(path):
        for file in files:
            ok = 0
            if re.match(regex, file):
                ok += 1

            try:
                f = open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore')
                for line in f:
                    tmp_line = line.strip()
                    if re.match(regex, tmp_line):
                        ok += 1
                        break
                f.close()
            except IOError:
                print("Unable to open file: " + file)

            if ok == 1:
                print(file)
            elif ok == 2:
                print(">>" + file)


if __name__ == '__main__':
    print("EX1:", extract_words('Hello, world!'))
    print("EX2:", extract_words_regex('[a-zA-Z0-9]', 'Hello, world!', 4))
    print("EX3:", extract_words_regex_list(['\w+', '\d+'], 'Hello, world! 123'))
    print("EX4:", extract_elements_by_attrs('test.xml', {'seven': 'engine'}))
    print("EX5:", extract_elements_by_attrs2('test.xml', {'seven': 'engine', 'sky': 'happily'}))
    print("EX6:", censor_words('Ana si cu Ioana merg acasa'))
    print("EX7:", is_valid_cnp('5010621270820'))
    find_files('d:\\Desktop\\Facultate\\SEMESTRUL_1\\Python\\Python_2022', '\w+')
