raise Exception('Not complete')

# 18720 1e6
'''
20      1-2
100     2-3
600     3-4
0       4-5
18000   5-6
50000   6-7
'''
def answer():
    '''Run this to get the answer.'''
    count = 0
    for n in range(int(1e5),int(1e6)):
        if n % 10 == 0: 
            continue
        r = int(str(n)[::-1])
        m = n + r
        while m:
            if(m%2 == 0):
                break
            m //= 10
        else:
            count += 1
            
    return count


print(answer())


 
            
        
