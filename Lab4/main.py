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

        for (root, directories, files) in os.walk(my_path):
            for file_name in files:
                path_extension.add(file_name.split('.')[-1])

    except NotADirectoryError:
        print("Given path is not a directory: " + my_path)

    return sorted(path_extension)


"""
EX2: Să se scrie o funcție ce primește ca argumente două căi: director si fișier. 
Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a 
fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A. 
"""


