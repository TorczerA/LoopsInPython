from time import sleep
from os import system, name  # For defining the clear() function


def clear():  # THIS FUNCTION IS FOR CLEARING THE SCREEN JUST LIKE clrscr() in C++
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


while 1:
    print("----------------------------Loops Program-----------------------------------")
    print()
    print("--------------------------------Menu----------------------------------------")
    print("1. for Loop")
    print("2. while Loop")
    print("3. Nested Loops")
    print("4. Exit")
    ch = int(input("Please choose your option -> "))
    if ch == 4:
        print("Loops Program Exiting")
        sleep(1)
        print("-------")
        print("--BYE--")
        print("-------")
        sleep(1)
        break
    elif ch == 1:
        print("--This program will demonstrate how for loop works--")
        print("We will repeatedly take the input until user enters 1")
        print("Let us start taking the Inputs")
        for i in range(0, 1000):
            try:
                num = int(input("-> "))
            except ValueError as e:
                print("Oops.. You entered a character string. We need numbers")
            if num == 1:
                break
            else:
                continue
        print("You entered 1 after", i, "entries")
        print("Do you want to see the source code for the mechanism ? (y/n)")
        flag1 = input("-> ")
        if flag1 == 'y' or flag1 == 'Y':
            clear()
            print("------------------------Source Code-------------------")
            print(""' print("Let us start taking the Inputs")')
            print("for i in range(0,1000):")
            print("    try:")
            print(""'        num=int(input("-> "))')
            print("    except ValueError as e:")
            print(""'        print("Oops.. You entered a character string. We need numbers")')
            print("    if num==1:")
            print("          break")
            print("    else")
            print("          continue")
            print(""'print("You entered 1 after",i,"entries")')
            print('------------------------------------------------------')
        else:
            pass
    elif ch == 2:
        print("--This program will demonstrate how while loop works--")
        print("We will repeatedly take the input until user enters 1")
        print("Let us start taking the Inputs")
        num = 0
        count = 0
        while num != 1:
            try:
                num = int(input("-> "))
                count = count + 1
            except ValueError as e:
                print("Oops.. You entered a character string. We need numbers")

            if num == 1:
                break
            else:
                continue
        print("You entered 1 after", count, "entries")
        print("Do you want to see the source code for the mechanism ? (y/n)")
        flag1 = input("-> ")
        if flag1 == 'y' or flag1 == 'Y':
            clear()
            print("------------------------Source Code-------------------")
            print(""' print("Let us start taking the Inputs")')
            print("num=0")
            print("count=0")
            print("while num!=1:")
            print("    try:")
            print(""'     num=int(input("-> "))')
            print("       count=count+1")
            print("    except ValueError as e:")
            print(""'     print("Oops.. You entered a character string. We need numbers")')
            print("    if num==1:")
            print("       break")
            print("    else")
            print("       continue")
            print(""'print("You entered 1 after",i,"entries")')
            print('------------------------------------------------------')
        else:
            pass
    elif ch == 3:
        print("--This program will demonstrate how Nested loops work--")
        print("We will print a star pattern to see how nested loops can be used")
        rows = int(input("Please input the number of rows you want -> "))
        for i in range(0, rows + 1):
            for j in range(0, i):
                print("*", end='')
            print()

        print("Do you want to see the source code for the mechanism ? (y/n)")
        flag1 = input("-> ")
        if flag1 == 'y' or flag1 == 'Y':
            clear()
            print("------------------------Source Code-------------------")
            print(""'rows=int(input("Please input the number of rows you want -> "))')
            print("for i in range(0,rows+1):")
            print("    for j in range(0,i):")
            print(""'        print("*",end='')')
            print("    print()")
            print('------------------------------------------------------')
        else:
            pass
