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
print('\n')


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
print('\n')


'''
    EX3: Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited 
    with b, a - b, b - a)
'''

def a_intersect_b(a, b):
    list = []
    for x in a:
        for y in b:
            if x == y:
                list.append(x)
                break
    return list


def a_reunited_b(a, b):
    return list(dict.fromkeys(a + b))


def a_minus_b(a, b):
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
print('\n')


'''
    EX4: Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) 
    and a start position (integer). The function will return the song composed by going though the musical notes 
    beginning with the start position and following the moves given as parameter.
'''

def compose(musical_notes, moves, start_pos):
    song = []
    current_pos = start_pos
    for move in moves:
        song.append(musical_notes[current_pos])
        current_pos = (current_pos + move) % len(musical_notes)
    song.append(musical_notes[current_pos])
    return song


print("EX4: ",  compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
print('\n')


'''
    EX5: Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the 
    elements under the main diagonal with 0 (zero).
'''

