import math
from collections import defaultdict
from bitstring import BitArray

primes = [2, 3, 5, 7, 11, 13, 17, 19]
primes_ba = BitArray()


def init_prime_bitarray(maxnum):
    """Initialize a bitarray with the supplied length, and find primes with
    a prime sieve."""
    global primes_ba
    maxnum += 1
    primes_ba = BitArray(maxnum)
    primes_ba.set(1)
    primes_ba[0], primes_ba[1] = [0, 0]
    for i in [2] + list(range(3, maxnum, 2)):
        if primes_ba[i]:
            for j in range(i + i, maxnum, i):
                primes_ba[j] = 0


def bitarray_to_list():
    """Return the primes in the initialized primes_ba as a list."""
    global primes, primes_ba
    if primes_ba:
        primes = [num for num, isprime in enumerate(primes_ba) if isprime]


def possible_divisors(num):
    """Generate a list of primes that are less than or equal to the square \
        root of the supplied number."""
    maxnum = int(math.sqrt(num))
    append_primes_until(maxnum)
    for i in primes:
        if i > maxnum:
            break
        yield i


def next_prime():
    """Add the next prime to the modules list of primes."""
    next = primes[-1] + 2
    while next != primes[-1]:
        for i in possible_divisors(next):
            if not next % i:
                break
        else:
            primes.append(next)
            continue
        next += 1


def prime_after(num):
    """Return the smallest prime greater than a given number."""
    if primes[-1] > num:
        for i in primes:
            if i > num:
                return i
    else:
        append_primes_until(num + 1)
        return primes[-1]


def append_primes_until(max):
    """Add to the primes list until the supplied max is reached.
    E.g. if max is 12, 13 will be added since prime 11 is less than 12."""
    while primes[-1] < max:
        next_prime()


def append_nth_prime(n):
    """Add primes to the prime list until there are at least n primes."""
    while len(primes) < n:
        next_prime()


def get_nth_prime(n):
    """Return the Nth prime."""
    append_nth_prime(n)
    return primes[n - 1]


def prime_factors(num):
    """Return a dictionary with a number's factors and their powers."""
    factors = defaultdict(int)
    for i in possible_divisors(num):
        while not num % i:
            num /= i
            factors[i] += 1
    if num > 1:
        factors[num] += 1
    return factors


def is_prime(num):
    """Checks if a number is prime looking for divisors from primes up to its
    square root.
    """
    num = abs(num)
    if num < 2: return False

    for divisor in possible_divisors(num):
        if not num % divisor:
            return False
    return True

def gcd(a, b):
    """Return the greatest common divisor of two integers."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return the least common multiple of two integers."""
    return a // gcd(a, b) * b


