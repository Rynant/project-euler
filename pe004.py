'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def palindromic_products():
    for m in range(100, 1000):
        for n in range(100, 1000):
            product = str(m * n)
            if product == product[::-1]:
                yield int(product)

def answer():
    return max(palindromic_products())

if __name__=='__main__':
    print(answer())