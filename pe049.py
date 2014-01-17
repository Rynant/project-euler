from collections import defaultdict
import primes

def answer():
    primes.append_primes_until(9999)
    prime_list = [x for x in primes.primes if x > 1000]
    prime_permutations = defaultdict(lambda:[])
    
    for i in prime_list: prime_permutations[''.join(sorted(str(i)))] += [i]
    
    for p in prime_permutations:
        prime_group = defaultdict(lambda:[])
        pp = prime_permutations[p]
        for n in range(len(pp)-1):
            for m in range(n+1, len(pp)):
                prime_group[abs(pp[m]-pp[n])] += [pp[n], pp[m]]
        for g in prime_group:
            pg = prime_group[g]
            if len(pg) >= 3:
                for a in range(0,len(pg)-2):
                    for b in range(a+1, len(pg)-1):
                        for c in range(b+1, len(pg)):
                            if (pg[a] - pg[b]) == (pg[b] - pg[c]):
                                return '{0}{1}{2}'.format(pg[a], pg[b], pg[c])
        
                    
if __name__=='__main__':
    print(answer())