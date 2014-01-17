import primes as p
from math import log10
p.init_prime_bitarray(1000000)
primes = p.primes_ba

def is_circular(n):
    global primes
    l = int(log10(n))
    for x in range(l):
        n = (n%10)*10**(l) + n//10
        if primes[n]:
            primes[n] = 0
        else:
            break
    else:
        return l + 1
    return 0

def answer():
    return sum(is_circular(a) for a, isprime in enumerate(primes) if isprime)
    # Answer is 55, this is giving 56

if __name__=='__main__':
    print(answer())