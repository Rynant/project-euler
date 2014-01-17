import primes

def answer():
    # (a, b, <consecutive prime count>)
    max_count = (0, 0, 0)
    
    def quadradic_calc(n, a, b):
        return n**2 + a*n + b
    
    def consecutive_prime_count(a, b):
        n = 0
        while True:
            if not prime_ba[quadradic_calc(n, a, b)]:
                return n
            n += 1
    
    primes.init_prime_bitarray(20000)
    prime_ba = primes.primes_ba
    primes.bitarray_to_list()
    prime_list = [p for p in primes.primes if p < 1000]
    neg_prime_list = [-1 * p for p in prime_list]
    
    for a in neg_prime_list:
        for b in prime_list:
            count = consecutive_prime_count(a, b)
            if(count > max_count[2]):
                max_count = (a, b, count)
    
    return max_count[0] * max_count[1]

if __name__=='__main__':
    print(answer())