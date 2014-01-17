import math

def hypotenuse(a,b):
    return math.sqrt(a**2 + b**2)

def answer():
    # (p, count)
    max_count = (0, 0)
    for p in range(12,1001, 2):
        count = 0
        for a in range(1, p//2):
            for b in range(1, a):
                c = hypotenuse(a, b)
                if c == int(c) and a + b + c == p:
                    count += 1
        if count > max_count[1]:
            max_count = (p, count)
    
    return max_count[0]


if __name__=='__main__':
    print(answer())