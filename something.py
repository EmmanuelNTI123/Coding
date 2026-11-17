# plustecken
n=int(input("antal rader? "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("+", end="")
    print()    # avslutar raden