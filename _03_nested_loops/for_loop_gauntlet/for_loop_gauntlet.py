"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    for i in range(101):
        print (i)
    for i in range(100,-1,-1):
        print (i)
    for i in range(101):
        if i % 2 == 0:
            print(i)
    for i in range(101):
        if i % 2 == 1:
            print(i)
    for i in range(501):
        if i % 2 == 0:
            print(str(i) + " Even")
        else:
            print(str(i) + " Odd")
    for i in range(778):
        if i % 7 == 0:
            print(i)
    for i in range (13):
        ii = i
        i += 2009

        print("In " + str(i) + " I was " + str(ii))
    for k in range(3):
        for i in range(3):
            print(str(k) + " " + str(i))
    for i in range (3):
        i = i * 3
        a = i + 1
        b = i + 2
        c = i + 3
        print(str(a) + " " + str(b) + " " + str(c))


    for i in range(101):

        print(i, end = ' ')
        if i % 10 == 0:
            print()
    for i in range(6):
        print(" * ", end = " ")
        if i > 0:
            print(" * ", end=" ")
            if i > 1:
                print(" * ", end=" ")
                if i > 2:
                    print(" * ", end=" ")
                    if i > 3:
                        print(" * ", end=" ")
                        if i > 4:
                            print(" * ", end=" ")
                            if i > 5:
                                print(" * ", end=" ")
                            else:
                                print()
                        else:
                            print()
                    else:
                        print()
                else:
                    print()
            else:
                print()
        else:
            print()




    pass
