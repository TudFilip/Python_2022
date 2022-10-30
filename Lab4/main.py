import os
import sys

"""
EX1: Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul
dat ca parametru.
"""

def exercitiul_1(my_path: str):
    """"""
    path_extension = set()
    try:
        if not os.path.dirname(my_path):
            raise NotADirectoryError()
    except NotADirectoryError:
        print("Given path is not a directory: " + my_path)
    else:
        for (root, directories, files) in os.walk(my_path):
            for file_name in files:
                path_extension.add(file_name.split('.')[-1])

    return sorted(path_extension)


"""
EX2: Să se scrie o funcție ce primește ca argumente două căi: director si fișier. 
Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a 
fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A. 
"""

def exercitiul_2(input_director: str, input_file: str):
    """"""
    try:
        if not os.path.dirname(input_director):
            raise NotADirectoryError()
        if not os.path.isfile(input_file):
            raise FileNotFoundError()
        file = open(input_file, 'wt')
    except NotADirectoryError:
        print("Given path is not a directory: " + input_director)
    except FileNotFoundError:
        print("Given path is not a file: " + input_file)
    except OSError:
        print("Unable to open the file: " + input_file)
    else:
        for (root, directories, files) in os.walk(input_director):
            for file_name in files:
                if file_name.split('.')[0].startswith('A'):
                    file.write(os.path.abspath(file_name))


"""
EX3: Să se scrie o funcție ce primește ca parametru un string my_path.
Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. 
Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată 
descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. 
Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.
"""