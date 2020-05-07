cache = {}

def fib(n):
    if n <= 1:
        return n
    
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    
    return cache[n]

for i in range(100):
    print(fib(i))


# from order 2^n to order n