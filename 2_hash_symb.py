print("\n")

for y in range(1, 11):
    for x in range(1, 11):
        if(( x == 1 ) or ( x == 10 ) or ( y == 1 ) or ( y == 10 )):
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()

print("\n")
