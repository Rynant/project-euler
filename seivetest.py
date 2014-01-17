import primes

primes.init_prime_bitarray(100)
primes.bitarray_to_list()
ba = primes.primes_ba
print(ba)
print(primes.primes)

# Rotate list: a.insert(0,a.pop())
# Rotate a number: (n%10)*10**(int(math.log10(n))) + n/10
'''Rotate a digit.
l = int(math.log10(n))
a = [n]
for i in range(l):
     n = (n%10)*10**(l) + n/10
     a.append(n)
return a
'''
