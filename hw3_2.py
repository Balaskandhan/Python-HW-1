def count_frequency(mylist):
    unique_list = set(sorted(mylist))
    print("list to set is",unique_list)
    pydict = {}
    #count = 0
    for words in unique_list:
        count = 0
        for word in mylist:
            if(words == word):
                count = count +1
        pydict[words] = count
    return pydict

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist))