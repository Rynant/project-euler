import math, primes


def is_truncatable(primenum):
    digits = int(math.log10(primenum))
    left = right = primenum
    for i in range(digits):
        right = right // 10
        if right in primes.primes:
            left = left % 10**(int(math.log10(left)))
            if left not in primes.primes:
                break
        else:
            break
    else:
        return True

def answer():
    truncatable = [23]
    pr = 23

    while len(truncatable) < 11:
        pr = primes.prime_after(pr)
        if is_truncatable(pr):
            truncatable.append(pr)

    return sum(truncatable)

if __name__=='__main__':
    print(answer())