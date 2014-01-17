from primes import is_prime
from itertools import count

def answer():
    diag_total = 1
    diag_primes = 0.0
    current = 1
    for i in count(2, 2):
        for j in range(0, 4):
            current += i
            diag_primes += is_prime(current)
        diag_total += 4
        if diag_primes / diag_total < 0.1:
            return i + 1

if __name__=='__main__':
    print(answer())