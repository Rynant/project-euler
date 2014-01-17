
def answer():
    return sum(n for n in range(1001) if not(n%3) or not(n%5))
    
if __name__=='__main__':
    print(answer())