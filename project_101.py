import random
print(input("press y to roll the dice and n to exit: "))
response = "y"
while response == "y":
    no = random.randint(1 , 6)
    if no == 1:
        print("[-----] [     ] [  0  ] [     ] [-----]")
        print(input("press y to roll the dice and n to exit: "))
    elif no == 2:
        print("[-----] [     ] [  00  ] [     ] [-----]")
        print(input("press y to roll the dice and n to exit: "))
    elif no == 3:
        print("[-----] [  0  ] [  0  ] [  0  ] [-----]")
        print(input("press y to roll the dice and n to exit: "))
    elif no == 4:
        print("[-----] [0   0] [     ] [0   0] [-----]")
        print(input("press y to roll the dice and n to exit: "))
    elif no == 5:
        print("[-----] [0   0] [  0  ] [0   0] [-----]")
        print(input("press y to roll the dice and n to exit: "))
    elif no == 6:
        print("[-----] [0   0] [0   0] [0   0] [-----]")
        print(input("press y to roll the dice and n to exit: "))
    else:
        print("please type y or n")