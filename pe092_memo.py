#raise Exception('Not complete')
'''
count = 0
for n in range(1,10000000):
    while 1:
        n = sum(int(c)**2 for c in str(n))
        if n == 1 or n == 89:
            count += 1 if n == 89 else 0
            break
print(count)
''' 
digit_list = {'89':1}

def number_digits(number):
    while number:
        yield number % 10
        number = number // 10

def sum_sqr(nums):
    return sum(d**2 for d in nums)

def is_happy(number):
    dlist = [sorted(number_digits(number))]
    while dlist[-1] != [1] and dlist[-1] not in digit_list:
        dlist += [sorted(number_digits(sum_sqr(dlist[-1])))]
    if dlist[-1] == [1]:
        return 0
    else:
        return 1
        
        
    
def answer():
    return sum(is_happy(n) for n in range(1, 100000))

#print(answer())