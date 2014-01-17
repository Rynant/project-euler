raise Exception('Not complete')

from re import findall

def fracs():
    for n in range(1,2000000):
        if not findall('(?P<digit>\d)(?P=digit){2}', str(n)):
            yield (1.0/n)

def answer():
    return sum(fracs())

if __name__=='__main__':
    print(answer())