import os

file_list = os.listdir("D:\Python_lekcje")
print(file_list)
save_path = os.getcwd()
os.chdir("D:\Python_lekcje")
print(os.getcwd())
table = str.maketrans(dict.fromkeys('jpg'))
for i in file_list:
    os.rename(i, i.translate(table))
