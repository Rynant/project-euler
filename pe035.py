import primes as p
from math import log10
p.init_prime_bitarray(1000000)
p.bitarray_to_list()
primes = set(p.primes)

def get_rotations(n):
    rotations = set([n])
    l = int(log10(n))
    for x in range(l):
        n = (n%10)*10**(l) + n//10
        rotations.add(n)
    return rotations

def answer():
    return sum(1 for a in primes if get_rotations(a).issubset(primes))
    
if __name__=='__main__':
    print(answer())