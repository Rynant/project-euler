def answer():
    pandigits = set('123456789')
    max = 0
    
    for i in range(9000, 9999, 3):
        p = str(i) + str(i*2)
        if len(p) == 9 and set(p) == pandigits and int(p) > max:
            max = int(p)
    
    return max

if __name__=='__main__':
    print(answer())