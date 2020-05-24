import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_gen(n):
    if n < 2:
        return n
    return fib_gen(n-1) + fib_gen(n-2)

def fibbo(n):
    fib_cache = [0, 1, 1]

    for _ in range(2, n): 
        fib_cache.append(fib_cache[-1] + fib_cache[-2])
    return(fib_cache)

print([fib_gen(n) for n in range(8)])

#print(fib_gen.cache_info())

val = 8
print("{} is fib of {}".format(fibbo(val), val))
