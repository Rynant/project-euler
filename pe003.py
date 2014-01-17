def answer():
    num = 600851475143
    x = 3
    while num != 1:
        if not num % x:
            num //= x
        else:
            x += 1
    return x

if __name__=='__main__':
    print(answer())