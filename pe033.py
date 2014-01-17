from primes import gcd

def answer():
    numerator = denominator = 1
    
    for i in range(10, 100):
        if not i % 10: continue
        for j in range(i+1, 100):
            if not j % 10: continue
            k, l = str(i), str(j)
            if(k.find(l[0]) >= 0):
                k, l = float(k[(k.find(l[0])+1)%2]), float(l[1])
            elif(k.find(l[1]) >= 0):
                k, l = float(k[(k.find(l[1])+1)%2]), float(l[0])
            else: continue
            if(i / j == k / l):
                numerator *= k
                denominator *= l
    
    return denominator / gcd(numerator, denominator)

if __name__=='__main__':
    print(answer())