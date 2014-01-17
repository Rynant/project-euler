import primes


def permutations(digitlist, numstring=''):
    if len(digitlist) == 1:
        if digitlist[0] % 2 and digitlist[0] % 5:
            yield int(numstring + str(digitlist[0]))
    for d in digitlist:
        remaining = list(digitlist)
        remaining.remove(d)
        ns = numstring + str(d)
        for y in permutations(remaining, ns):
            yield y


def answer():
    for length in range(7, 0, -1):
        digits = range(length, 0, -1)
        for p in permutations(digits):
            if primes.is_prime(p):
                return p

if __name__=='__main__':
    print(answer())
