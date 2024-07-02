import time
def sigma():
    
    name = ""



    while len(name)==0:
       name = str(input("enter your name: "))

    time.sleep(1)
    print("hello mr", name)
    time.sleep(1)
    reply = str(input("would you help anyone in need? (yes, no): "))
    time.sleep(1)

    if reply == "yes":
        print('you are a sigma')

    elif reply == "no":
        print('you damn kid')
     
    else:
        print('not an ideal answer')
        retry = str(input('you wanna retry? (if yes type yes): '))
         
        if retry == 'yes':
          time.sleep(1)
          sigma()
        else:
          time.sleep(1)
          print('okay then, function out!')


sigma()