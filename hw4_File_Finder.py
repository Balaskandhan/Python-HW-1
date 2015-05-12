'''
Created on May 7, 2015

@author: balas
'''
import os
print(os.listdir('E:\\'))
search_path = input("enter the directory you want to search for: ")
#serach_path_now = search_path + ":"
#print(dir_path_now)
file_name = input("enter the name of the file you want to search for")
file_path = ""#os.path.join(dir_path,file_name)
if os.path.isdir(search_path):
    for paths in search_path:
        file_path = os.path.join(search_path,file_name)
        if os.path.isfile(file_path):
            print("Your file is found in")
            print(file_path)
            break
    else:
        print("No such file in")
        #print(file_path)
     
else:
    print("No such directory")