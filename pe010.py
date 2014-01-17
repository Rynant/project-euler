from bitstring import BitArray

def answer():
    ba = BitArray(2000000)
    ba.set(1)
    for i in range(4, 2000000, 2):
        ba[i] = 0
    
    for i in range(3, 2000000, 2):
        if ba[i]:
            for j in range(i + i, 2000000, i):
                ba[j] = 0
    
    return sum(i for i in range(3, 2000000, 2) if ba[i]) + 2
    
if __name__=='__main__':
    print(answer())
