raise Exception('Not complete')

count = 0
for n in range(1,10000000):
    while 1:
        n = sum(int(c)**2 for c in str(n))
        if n == 1 or n == 89:
            count += 1 if n == 89 else 0
            break
print(count)
    
