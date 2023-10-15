import random


response="y"

while response == "y":
    dice= random.randint(1,6)
    if (dice == 1):
        print("1")
        r=input("Enter y to continue and n to exit")
        response = r
    
    elif (dice == 2):
        print("2")
        r=input("Enter y to continue and n to exit")
        response  = r

    elif (dice == 3):
        print("3")
        r=input("Enter y to continue and n to exit")
        response = r

    elif (dice == 4):
        print("4")
        r=input("Enter y to continue and n to exit")
        response = r

    elif (dice == 5):
        print("5")
        r=input("Enter y to continue and n to exit")
        response = r

    else:
        print("6")
        r=input("Enter y to continue and n to exit")
        response = r