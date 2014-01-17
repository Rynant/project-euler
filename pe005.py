'''
Project Euler solution template.
'''
#raise Exception('Not complete')
from primes import lcm


def answer():
    n = 2
    for m in range(3,20):
        n = lcm(m, n)
    return n


if __name__=='__main__':
    print(answer())