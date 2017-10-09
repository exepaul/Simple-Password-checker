import sys

passcheck = input("Enter a password to check: ")

checking=set(passcheck)

passlength = len(passcheck)

points=0

symbols = {'!','$','%','^','&','*','(',')','-','_','=','+'}
qwerty = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]




if passlength <8 or passlength >24:
    print("ERROR. Password must be between 8-24 characters long")


else:

    for i in qwerty:

        if i in passcheck:
            points-=15
            print("your password contain form of 'QWERTY' , Don't use weak password.")
            print(points)
            sys.exit()

if any(i.islower() for i in checking) or any(i.isupper() for i in checking) or any(i for i in checking if i in symbols) or any(i.isdigit() for i in checking):
    points+=5


if any(i.islower() for i in checking) and any(i.isupper() for i in checking) and any(i.isdigit() for i in checking):
    points+=15

print(points)





