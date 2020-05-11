import math
import random

def slowfun(x, y, cache={}):
    v = math.pow(x, y)

    if v not in cache:
        cache[v] = math.factorial(v)
    v = cache[v]

    v //= (x + y)
    
    v %= 982451653

    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
