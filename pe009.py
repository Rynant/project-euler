'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def is_triplet(a,b,c):
    return (a**2 + b**2) == c**2

def answer():
    for a in range(1,999):
        for b in range(2,1000):
            c = 1000 - a - b
            if is_triplet(*sorted([a,b,c])):
                return a*b*c

if __name__=='__main__':
    print(answer())