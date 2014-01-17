
def permutations(digitlist, numstring=''):
    if len(digitlist) == 1:
        yield numstring + digitlist[0]
    for d in digitlist:
        remaining = list(digitlist)
        remaining.remove(d)
        ns = numstring + d
        for y in permutations(remaining, ns):
            yield y

def answer():
    fib = [2, 3, 5, 7, 11, 13, 17]
    position = range(0, 7)
    total = 0
    
    for p in permutations(list('0123456789')):
        if p[0] == '0': continue
        check = True
        for i in reversed(position):
            if int(p[i+1:i+4]) % fib[i]:
                check = False
                break
        if check:
            total += int(p)
    
    return total

if __name__=='__main__':
    print(answer())
