try:
    n = int(input('enter: '))
    d = int(input('enter: '))
    r = n//d
except ZeroDivisionError as e:
    print(e)
    print("you cant divide by zero idiot")
except ValueError as e:
    print(e)
    print('enter a number please')
except Exception as e:
    print(e)
    print("something went galat")
else:
    print(r)
finally: 
    print('this will always execute')