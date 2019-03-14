import os

file_list = os.listdir("Ścieżka pliku / Path directory")
save_path = os.getcwd()
os.chdir("Ścieżka pliku / Path directory")
table = str.maketrans(dict.fromkeys('znaki jakie mają zostać usunięte / chars to remove'))

for file_name in file_list:
    os.rename(file_name, file_name.translate(table))
 
os.chdir(save_path)
