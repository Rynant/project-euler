from itertools import count

ispent = lambda n: ((24*n + 1)**0.5 + 1) % 6 == 0
pent = lambda n: (3*n**2 - n)/2

def answer():
    for j in count(2):
        pj = pent(j)
        for k in range(j, 0, -1):
            pk = pent(k)
            if ispent(pj-pk) and ispent(pj+pk):
                return pj-pk

'''
5482660
'''


if __name__=='__main__':
    print(answer())
