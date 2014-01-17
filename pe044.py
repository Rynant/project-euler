
def answer():
    pents = set((3*n**2-n)/2 for n in range(1, 2500))
    for d in (j-k for j in pents for k in pents if j-k in pents and j+k in pents):
        return d


if __name__=='__main__':
    print(answer())