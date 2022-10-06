'''
    EX1: Cel mai mare divizor comun al unor numere citite de la tastatura
'''
# def GCD(x, y):
#     while x != y:
#         if x > y:
#             x = x - y
#         else:
#             y = y - x
#     return x
#
#
# def exercise1():
#     first_number = int(input('Introduceti un numar: '))
#     second_number = int(input('Introduceti un numar: '))
#     gcd = GCD(first_number, second_number)
#     third_number = int(input('Introduceti un numar: '))
#     while third_number != 0:
#         gcd = GCD(gcd, third_number)
#         third_number = int(input('Introduceti un numar: '))
#     print("Cel mai mare divizor comun este:" + str(gcd))
#
#
# exercise1()


'''
    EX2: Vocalele dintr-un string
'''
# vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
#
# def vowels_in_string(message):
#     vowels = 0
#     for char in message:
#         if char in vowel_list:
#             vowels += 1
#     return vowels
#
# text = input('Cititi stringul: ')
# print('In text sunt ' + str(vowels_in_string(text)) + ' vocale')


'''
    EX3: Write a script that receives two strings and prints the number of occurrences of the first string in the 
    second.
'''
# first_string = input('Stringul in care se face cautarea: ')
# second_string = input('Stringul care se cauta in stringul anterior: ')
#
# occurrences = 0
# second_string_length = len(second_string)
# for index in range(len(first_string)):
#     if first_string[index:index + second_string_length] == second_string:
#         occurrences += 1
#
# print('Numarul de aparitii al aldoilea string in primul este: ' + str(occurrences))


'''
    EX4: Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
'''
# string = input('Introduceti textul de formatat: ')
# format_string = string[0].lower()
#
# for index in range(1,len(string)):
#     if string[index].isupper():
#         format_string += '_' + string[index].lower()
#     else:
#         format_string += string[index]
#
# print(format_string)


'''
    EX5: Given a square matrix of characters write a script that prints the string obtained by going through the matrix 
    in spiral order.
'''
# matrix = [['f', 'i', 'r', 's'],
#           ['n', '_', 'l', 't'],
#           ['o', 'b', 'a', '_'],
#           ['h', 't', 'y', 'p']]
# final_text = ''
#
# first_row = 0
# first_column = 0
# last_row = len(matrix) - 1
# last_column = len(matrix[0]) - 1
#
# while first_row <= last_row and first_column <= last_column:
#     for i in range(first_column, last_column + 1):
#         final_text += matrix[first_row][i]
#
#     for i in range(first_row + 1, last_row + 1):
#         final_text += matrix[i][last_column]
#
#     for i in range(last_column - 1, first_column - 1, -1):
#         final_text += matrix[last_row][i]
#
#     for i in range(last_row - 1, first_row, -1):
#         final_text += matrix[i][first_column]
#
#     first_row += 1
#     first_column += 1
#     last_row -= 1
#     last_column -= 1
#
# print(final_text)


'''
    EX6: Write a function that validates if a number is a palindrome.
'''
# number = int(input('Introdu un numar: '))
# aux = number
# rev_number = 0
#
# while aux != 0:
#     c = aux % 10
#     rev_number = rev_number * 10 + c
#     aux = aux // 10
#
# if number == rev_number:
#     print('Numarul este palindrom')
# else:
#     print('Numarul nu este palindrom')


'''
    EX7: Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this 
    function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract 
    only the first number that is found.
'''
# message = input('Introduceti mesajul dorit: ')
#
#
# def get_number_from_message(text):
#     numar_extras = 'none'
#     for char in text:
#         if char.isdigit():
#             if numar_extras == 'none':
#                 numar_extras = 0
#             numar_extras *= 10
#             numar_extras += int(char)
#         if numar_extras != 'none' and not char.isdigit():
#             return numar_extras
#     if numar_extras != 'none':
#         return numar_extras
#
#
# print(get_number_from_message(message))


'''
    EX8: Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary 
    format is 00011000, meaning 2 bits with value "1"
'''
# number = int(input('Introduceti un numar: '))
#
#
# def get_bits_with_value_1_from_number(x):
#     counter = 0
#     while x >= 1:
#         if x % 2:
#             counter += 1
#         x = x // 2
#     return counter
#
#
# print(get_bits_with_value_1_from_number(number))


'''
    EX9: Write a functions that determine the most common letter in a string. For example if the string is "an apple is 
    not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. 
    Casing should not be considered "A" and "a" represent the same character.
'''
# def most_common_letter(text):
#     letters_occurrences = {}
#     for char in str(text):
#         if char.encode('ascii').isalpha():
#             if char not in letters_occurrences:
#                 letters_occurrences[char] = 1
#             else:
#                 letters_occurrences[char] += 1
#
#     return max(letters_occurrences, key=letters_occurrences.get), max(letters_occurrences.values())
#
#
# string = input('Introduceti textul: ')
# result = most_common_letter(string)
#
# print(result[0] + ' - ' + str(result[1]))


'''
    EX10: Write a function that counts how many words exists in a text. A text is considered to be form out of words 
    that are separated by only ONE space. For example: "I have Python exam" has 4 words.
'''
def get_number_of_words(text) :
    return len(text.split(" "))


string = input('Introduceti textul: ')

print('Numarul de cuvinte din text este de: ' + str(get_number_of_words(string)))









