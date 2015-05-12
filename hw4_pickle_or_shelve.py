def pickle_data():
    read_file = open("picles.txt","br")
    return_list = pickle.load(read_file)
    print("Data_Pickled:\n",return_list)
    newfile.close()

import pickle
newfile = open("picles.txt","bw")
name = input("Enter your name:")
age = input("Enter your age:")
country_of_origin = input("Enter your country_of_origin:")
mylist = [name,age,country_of_origin]
pickle.dump(mylist,newfile)
newfile.close()
pickle_data()
