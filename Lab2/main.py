'''
    EX1: Write a function to return a list of the first n numbers in the Fibonacci string.
'''

def fibonacci(n):
    '''Return a list of the first n numbers in the Fibonacci string.'''
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo


print('EX1: Lista primelor 10 numere din sirul Fibonacci: ', fibonacci(10))
print()


'''
    EX2: Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
'''

def is_prime(n):
    '''Return True if n is prime.'''
    if n < 2:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


def primes_in_list(lst):
    '''Return a list of the prime numbers found in a list.'''
    return [x for x in lst if is_prime(x)]


print('EX2: Lista numerelor prime din lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: ', primes_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print()


'''
    EX3: Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited 
    with b, a - b, b - a)
'''

def a_intersect_b(a, b):
    ''''''
    list = []
    for x in a:
        for y in b:
            if x == y:
                list.append(x)
                break
    return list


def a_reunited_b(a, b):
    ''''''
    return list(dict.fromkeys(a + b))


def a_minus_b(a, b):
    ''''''
    list = []
    for i in range(len(a)):
        if b.count(a[i]) == 0:
            list.append(a[i])
    return list


list1 = [1, 2, 3, 4, 8, 9, 10]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("EX3")
print("Lista [1, 2, 3, 4, 8, 9, 10] intersectata cu lista [1, 2, 3, 4, 5, 6, 7]: ", a_intersect_b(list1, list2))
print("Lista [1, 2, 3, 4, 8, 9, 10] reunita cu lista [1, 2, 3, 4, 5, 6, 7]: ", a_reunited_b(list1, list2))
print("Lista [1, 2, 3, 4, 8, 9, 10] minus lista [1, 2, 3, 4, 5, 6, 7]: ", a_minus_b(list1, list2))
print("Lista [1, 2, 3, 4, 5, 6, 7] minus lista [1, 2, 3, 4, 8, 9, 10]: ", a_minus_b(list2, list1))
print()


'''
    EX4: Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) 
    and a start position (integer). The function will return the song composed by going though the musical notes 
    beginning with the start position and following the moves given as parameter.
'''

def compose(musical_notes, moves, start_pos):
    ''''''
    song = []
    current_pos = start_pos
    for move in moves:
        song.append(musical_notes[current_pos])
        current_pos = (current_pos + move) % len(musical_notes)
    song.append(musical_notes[current_pos])
    return song


print("EX4: ",  compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
print()


'''
    EX5: Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the 
    elements under the main diagonal with 0 (zero).
'''

def change_matrix(matrix):
    ''''''
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i > j:
                matrix[i][j] = 0
    return matrix


def print_matrix(matrix):
    ''''''
    i = 0
    while i != len(matrix):
        print(matrix[i])
        i += 1


test_matrix = [[1, 2, 3, 4, 6],
     [5, 6, 7, 8, 10],
     [9, 1, 2, 3, 7],
     [4, 5, 6, 7, 5],
     [2, 5, 10, 6, 7]]


print("EX5:")
print_matrix(change_matrix(test_matrix))
print()


'''
    EX6: Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list 
    containing the items that appear exactly x times in the incoming lists. 
'''

def search(x, *lists):
    ''''''
    final_list = []
    for list in lists:
        final_list += list

    items = []
    for number in final_list:
        if final_list.count(number) == x and items.count(number) == 0:
            items.append(number)
    items.sort()
    return items


print("EX6: ", search(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
print()


'''
    EX7: Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 
    elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second 
    element will be the greatest palindrome number.
'''

def is_palindrome(x: int):
    ''''''
    aux = x
    pal = 0
    while aux != 0:
        pal = pal * 10 + aux % 10
        aux = aux // 10

    if x == pal:
        return True
    return False


def palindromes_of_list(my_list: list):
    ''''''
    counter = 0
    greatest_palindrome = 0
    for number in my_list:
        if is_palindrome(number):
            counter += 1
            if number > greatest_palindrome:
                greatest_palindrome = number

    return counter, greatest_palindrome


print("EX7: ", palindromes_of_list([123454321, 23451, 898989, 234432, 10001, 454]))
print()


'''
    EX8: Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set 
    to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the 
    flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
'''

def string_characters(list_of_strings: list, flag: bool, x = 1):
    ''''''
    final_list = []
    for tmp_string in list_of_strings:
        tmp_list = []
        for char in tmp_string:
            divisible = ord(char) % x
            if flag:
                if divisible == 0:
                    tmp_list.append(char)
            else:
                if divisible != 0:
                    tmp_list.append(char)
        final_list.append(tmp_list)
    return final_list


print("EX8: ", string_characters(["test", "hello", "lab002"], False, 2))
print()


'''
    EX9: Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium 
    and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the 
    game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the 
    seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the
    closest row from the field.
'''

def unlucky_spectators(seats: list):
    ''''''
    spectators = []
    for seat_column in range(0, len(seats[0])):
        max_height = seats[0][seat_column]
        for seat_line in range(1, len(seats)):
            if seats[seat_line][seat_column] > max_height:
                max_height = seats[seat_line][seat_column]
            else:
                spectators.append([seat_line, seat_column])
    return spectators


stadium_seats = [[1, 2, 3, 2, 1, 1],
                [2, 4, 4, 3, 7, 2],
                [5, 5, 2, 5, 6, 4],
                [6, 6, 7, 6, 7, 5]]


print("EX9: ", unlucky_spectators(stadium_seats))
print()


'''
    EX10: Write a function that receives a variable number of lists and returns a list of tuples as follows: the first 
    tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, 
    etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 
'''

def tuples_from_lists(*input_lists: list):
    ''''''
    max_length = max(len(x) for x in input_lists)
    my_tuples = []
    for i in range(max_length):
        my_tuples.append([])
    for i in range(0, len(input_lists)):
        if len(input_lists[i]) < max_length:
            while len(input_lists[i]) != max_length:
                input_lists[i].append(None)
        for j in range(0, len(input_lists[i])):
            my_tuples[j].append(input_lists[i][j])
    return my_tuples


print("EX10: ", tuples_from_lists([1, 2, 3, 56, 23], [5, 6, 7], ["a", "b", "c"]))
print()


'''
    EX11: Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the 
    tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
'''

def order_tuples(input_tuples: list):
    ''''''
    return sorted(input_tuples, key=lambda x: x[1][2])


print("EX11: ", order_tuples([('abc', 'bcd'), ('abc', 'zza'), ('abc', 'ghi')]))
print()


'''
    EX12: Write a function that will receive a list of words as parameter and will return a list of lists of words, 
    grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
'''

def group_by_rhyme(input_list: list):
    rhymes = []
    existing_rhymes = []
    for i in range(len(input_list)):
        rhymes.append([])

    for word in input_list:
        last_2_letters = word[-2:]
        if last_2_letters not in existing_rhymes:
            existing_rhymes.append(last_2_letters)
            rhymes[existing_rhymes.index(last_2_letters)].append(word)
        else:
            rhymes[existing_rhymes.index(last_2_letters)].append(word)

    return rhymes


print("EX12: ", group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))





