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
                    file.write(input_director + '\\' + file_name + '\n')
        file.close()

"""
EX3: Să se scrie o funcție ce primește ca parametru un string my_path.
Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. 
Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată 
descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. 
Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.
"""

def exercitiul_3(my_path: str):
    """"""
    try:
        if not os.path.dirname(my_path):
            raise ValueError()
    except ValueError:
        return "Given parameter is neither a directory or a file"
    else:
        if os.path.isfile(my_path):
            try:
                f = open(my_path, 'rt')
                last_20_char = f.read()
                return last_20_char[-20:]
            except OSError:
                return "Unable to open the file: " + my_path
        else:
            extensions_counter = []
            for (root, directories, files) in os.walk(my_path):
                for file_name in files:
                    if len(extensions_counter) == 0:
                        aux = tuple((file_name.split('.')[-1], 1))
                        extensions_counter += tuple([aux])
                    elif file_name.split('.')[-1] in [ext[0] for ext in extensions_counter]:
                        for extension in extensions_counter:
                            if extension[0] == file_name.split('.')[-1]:
                                aux = tuple((file_name.split('.')[-1], extension[1] + 1))
                                del extensions_counter[extensions_counter.index((file_name.split('.')[-1], extension[1]))]
                                extensions_counter += tuple([aux])
                    else:
                        aux = tuple((file_name.split('.')[-1], 1))
                        extensions_counter += tuple([aux])

            return sorted(extensions_counter, reverse=True, key=lambda x: x[1])

# print(exercitiul_3('d:\Desktop\Facultate\SEMESTRUL_1\Python'))
"""
EX4: Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la 
linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
"""

def exercitiul_4():
    extensions = set()
    for file in os.listdir(sys.argv[1]):
        if os.path.isfile(os.path.join(sys.argv[1] + '\\', file)):
            extensions.add(file.split('.')[-1])
    return sorted(extensions)


"""
EX5: Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza o 
listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in 
fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director. Dacă target nu 
este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
"""

def exercitiul_5(target: str, to_search: str):
    """"""
    try:
        if not os.path.isfile(target) and not os.path.isdir(target):
            raise ValueError()
    except ValueError:
        return "ex5: 'target' is not a file or a directory: " + target
    else:
        if os.path.isfile(target):
            if to_search in os.path.splitext(os.path.basename(target))[0]:
                return "ex5: 'target' exists in 'to_search' file"
            else:
                return "ex5: 'target' does not exists in 'to_search' file"
        else:
            find_files = []
            for (root, directories, files) in os.walk(target):
                for file in files:
                    if to_search in file.split('.')[0]:
                        find_files.append(file.split('.')[0])
            return find_files


"""
EX6: Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește 
un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea 
fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.
"""

if __name__ == '__main__':
    print(exercitiul_4())
    print(exercitiul_5('d:\Desktop\Facultate\SEMESTRUL_1\Python', 'lab'))

