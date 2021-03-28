#!/usr/bin/env python3

from  os import system

system( "clear" )

#DATA

max_X = max_Y = 11
min_X = min_Y = 1

print("\n")

#LOGIC


for y in range( min_Y, max_Y ):

    if(( y == min_Y ) or ( y == max_Y - 1 )):
        
        for x in range( min_X - 1, max_X - 1 ):
            print("#", end = " " )
        print()
    
    
    else:
        
        for x in range( min_X, max_X):
            
            if(( x == min_X ) or (x == max_X - 1 )):
                print("#", end=" ")
            else:
                print(".", end=" ")
    
        print()

print("\n")
