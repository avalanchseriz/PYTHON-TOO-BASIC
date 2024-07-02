def strTolist(x, l=[]):
    x = str(x)
    l.append(x)
    return l


z = input("enter a srting: ")

x = strTolist(z)
print(x)