import primes

def answer():
    consecutive = []
    number = 646
    while len(consecutive) < 4:
        number += 1
        if len(primes.prime_factors(number)) == 4:
            consecutive.append(number)
        else:
            consecutive = []
    
    return consecutive[0]
    

if __name__=='__main__':
    print(answer())