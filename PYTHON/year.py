
'''import sys
sys.exit()    pārtrauc darbību'''


import math
gads_raw = input("Please enter Your birth year:")
if gads_raw.isdigit():
    gads = int(gads_raw)
    dekade = math.floor((gads % 100) / 10)
    if dekade < 5:
        print("You have born before 1952")
    else:
        print("You have born after 1950")
else:
    print("Please enter a number!")