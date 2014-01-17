
def answer():
    n = 100000
    samedigits = False
    while not samedigits:
        n += 1
        samedigits = True
        digits = set(str(n))
        for i in range(2, 7):
            if set(str(n * i)) != digits:
                samedigits = False
    return n

if __name__=='__main__':
    print(answer())