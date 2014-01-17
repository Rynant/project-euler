import math, primes


def is_truncatable(primenum):
    digits = int(math.log10(primenum))
    left = right = primenum
    for i in range(digits):
        right = right // 10
        if primes.primes_ba[right]:
            left = left % 10**(int(math.log10(left)))
            if not primes.primes_ba[left]:
                break
        else:
            break
    else:
        return True

def answer():
    truncatable = []
    primes.init_prime_bitarray(1000000)
    
    for pr in (i for i, isprime in enumerate(primes.primes_ba) if isprime):
        if pr < 11:
            continue
        if len(truncatable) == 11:
            break
        if is_truncatable(pr):
            truncatable.append(pr)
    
    return sum(truncatable)

if __name__=='__main__':
    print(answer())