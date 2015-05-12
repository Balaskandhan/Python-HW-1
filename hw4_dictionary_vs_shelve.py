import shelve
from datetime import datetime
my_dictionary = {'Name':'Balaskandhan',
                 'city':'west haven',
                 'Apt.no':'61',
                 'street name':'orange terrace',
                 'zip-code':'06516'}

start_time = datetime.now().time()
# print("time now is:",currenttime)
print("Starting time:",start_time)
print('06516' in my_dictionary.values())
for info in my_dictionary:
    print("The Information contained is {0} : {1}.".format(info,my_dictionary[info]))
end_time = datetime.now().time()    
print("End time:",end_time)

"""
Shelving
"""
print("{0}{1}{2}.".format(10*'-','Execution time for Shelve',10*'-'))
my_shelve = shelve.open("my_shelve")
my_shelve['information'] = {'Name':'Balaskandhan',
                 'city':'west haven',
                 'Apt.no':'61',
                 'street name':'orange terrace',
                 'zip-code':'06516'}
start_time_shelve = datetime.now().time()
print("Starting time:",start_time_shelve)
print('information' in my_shelve)
for info in my_shelve:
    print("The Information contained is {0} : {1}.".format(info,my_shelve[info]))
end_time_shelve = datetime.now().time()    
print("End time:",end_time_shelve)
