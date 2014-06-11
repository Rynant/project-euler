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

def number_digits(number):
    while number:
        yield number % 10
        number = number // 10


def is_happy(number):
    while True:
        if number == 1:
            return 0
        elif number == 89:
            return 1
        number = sum(d**2 for d in number_digits(number))

def answer():
    return sum(is_happy(n) for n in range(1, 100000))

#print(answer())