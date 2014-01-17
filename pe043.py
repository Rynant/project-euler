from itertools import permutations

def answer():
    primes = [2, 3, 5, 7, 11, 13, 17]
    pandigitals = [''.join(p) for p in permutations('0123456789')]
    total = 0
    position = range(0,7)
    
    for p in pandigitals:
        if p[0] == '0': continue
        for i in reversed(position):
            if int(p[i+1:i+4]) % primes[i]: break
        else: total += int(p)
    
    return total

if __name__=='__main__':
    print(answer())