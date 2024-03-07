from random import *
import time

def simulate():
    prev_a, prev_b = None, None
    first_condition, second_condition = 0, 0
    for _ in range(10000):
        seed(time.time())
        a = randint(1, 6)
        b = randint(1, 6)
        if a == 5 and prev_a == 5:
            first_condition += 1
        
        if b == 6 and prev_b == 5:
            second_condition += 1
        
        prev_a = a
        prev_b = b

    if first_condition > second_condition:
        return -1
    if second_condition > first_condition:
        return 1
    return 0

ans = 0
for i in range(100):
    ans += simulate()

print(ans)
    
