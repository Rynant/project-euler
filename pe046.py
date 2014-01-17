import primes as p

def get_squares():
    n = 1
    while True:
        yield n**2*2
        n += 1

def yield_while(generator, test):
    g = generator()
    n = next(g)
    while(test(n)):
        yield n
        n = next(g)
    return

def answer():
    i = 7
    while True:
        i += 2
        if not(p.is_prime(i)):
            for s in yield_while(get_squares, lambda x: x<i):
                if p.is_prime(i-s):
                    break
            else: return i
                    
if __name__=='__main__':
    print(answer())