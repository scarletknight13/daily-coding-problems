from math import *
def solve(num):
    power_of_2 = log2(num)
    return power_of_2 == int(power_of_2) and power_of_2 % 2 == 0


for i in range(1, 257):
    print(f"{i * 2} is {'not' if not solve(i * 2) else ''} a power of four" )


    
