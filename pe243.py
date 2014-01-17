from itertools import count
from functools import reduce
from primes import prime_factors

def totient(factors):
    return reduce(lambda prod, p: prod * p[0]**(p[1]-1) * (p[0]-1), factors, 1)

def answer():
    target = 15499 / 94744
    start = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23
    
    for n in count(start, start):
        factors = prime_factors(n).items()
        r = totient(factors) / (n - 1)
        if r < target:
            return n
            
if __name__=='__main__':
    print(answer())