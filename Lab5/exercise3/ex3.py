"""
Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list with
all the vowels in a given string.
"""


def vowels_in_string(string: str):
    return [character for character in string if character.lower() in "aeiou"]


def vowels_in_string_using_anonymous_function(string: str):
    anon_vowels_in_string = lambda input_string: [character for character in string if character.lower() in "aeiou"]
    return anon_vowels_in_string(string)


def vowels_string_using_filter(string: str):
    return list(filter(lambda char: char.lower() in "aeiou", string))


if __name__ == '__main__':
    print(vowels_in_string("Programming in Python is fun"))
    print(vowels_in_string_using_anonymous_function("Programming in Python is fun"))
    print(vowels_string_using_filter("Programming in Python is fun"))

