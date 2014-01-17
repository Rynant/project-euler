import math, collections


def answer():
    perims = []
    for a in range(1, 500):
        for b in range(1, a):
            c = math.sqrt(a**2 + b**2)
            if c == int(c):
                perims.append(a+b+c)
    
    return int(collections.Counter(
        p for p in perims if p <= 1000).most_common(1)[0][0])

if __name__=='__main__':
    print(answer())