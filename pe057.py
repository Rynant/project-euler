
def answer():
    a, b = 3, 2
    count = 0
    for _ in range(999):
        a, b = a + 2*b, a+b
        if len(str(a)) > len(str(b)):
            count += 1
    return count
        
if __name__=='__main__':
    print(answer())