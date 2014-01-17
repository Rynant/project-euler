import primes

def answer():
    primes.append_primes_until(2000000)
    return sum(x for x in primes.primes if x < 2000000)

import timeit
print '%.10f seconds' % timeit.timeit('print __main__.answer()', 'import __main__', number=1)
# 142913828922