from collections import OrderedDict, defaultdict
from math import sqrt

# Initialize prime factorization for numbers 0, 1 and 2
factor_dict = [[False, defaultdict(int)], [False, defaultdict(int)], [True, defaultdict(int, {2: 1})]]


# TODO need to alter for dictionary since {3: 2} counts as len 1
def get_primes():
    for isprime, fac in factor_dict:
        if isprime == 1: yield list(fac)[0]


def possible_divisors(n):
    maxdiv = int(sqrt(n))
    for p in get_primes():
        if p > maxdiv: break
        yield p


def addfactor():
    n = len(factor_dict)
    factor_dict.append([True, defaultdict(int)])
    for p in possible_divisors(n):
        if not n % p:
            factor_dict[n][0] = False
            factor_dict[n][1][p] = 1
            for prime, pwr in factor_dict[n//p][1].iteritems():
                factor_dict[n][1][prime] += pwr
            break
    else:
        factor_dict[n][1][n] = 1

def iterfactors():
    for f in factor_dict[1::]:
        yield f
    while True:
        addfactor()
        yield factor_dict[-1]


for facs in iterfactors():
    #print facs
    if len(factor_dict) > 1000000: break

