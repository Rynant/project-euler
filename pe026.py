def answer():
    '''
    Find the value of d  1000 for which 1/d contains the longest recurring cycle in
    its decimal fraction part.
    '''
    largest_repeat = (3, 1)
    
    for d in range(7, 1000, 2):
        if not d % 5: continue
        cycle = 1
        while 10**cycle % d != 1: cycle += 1
        if cycle > largest_repeat[1]: largest_repeat = (d, cycle)
    
    return largest_repeat[0]

if __name__=='__main__':
    print(answer())