def AddToDict(keys,values,dictionary):
    for i in range (len(keys)):
        if keys[i] not in dictionary:
            dictionary[keys[i]]=values[i]
        else:
            print(keys[i],"already exists in the dictionary and has a value", dictionary[keys[i]])
    print(dictionary)

keys = ["abhinav", "akshat", "bhavishya"]
values = [28,29,35]
dictionary = {"bhavishya":34, "vansh sehgal":25}

AddToDict(keys,values,dictionary)

