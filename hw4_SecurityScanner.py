import os
direct = '.'
file_name = input("Enter name of the file")
for dirName, subdirList, fileList in os.walk(direct):
    #print('Found directory: %s' % dirName)
    for fname in fileList :
        if file_name == fname:
            f = open(os.path.join(dirName,file_name))
            #print('\t%s' % file_name)
            #print("path is :",f)
            content = f.read()
            if 'password=' in content:
                print("Not secure")
            f.close()


