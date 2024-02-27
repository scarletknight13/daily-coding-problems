# Good morning! Here's your coding interview problem for today.

# This problem was asked by Indeed.

# Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.

from math import *
def solve(num):
    power_of_2 = log2(num)
    return power_of_2 == int(power_of_2) and power_of_2 % 2 == 0


for i in range(1, 257):
    print(f"{i * 2} is {'not' if not solve(i * 2) else ''} a power of four" )


    
