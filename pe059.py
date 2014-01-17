import re, itertools

with open('data/pe059_cipher1.txt') as f: msg = [int(x) for x in re.split('\D', f.read()) if x]

def answer():
    for key in itertools.product(*[range(97,123), range(97,123), range(97,123)]):
        xor =  [x^y for x, y in zip(msg, itertools.cycle(key))]
        if ''.join(chr(x) for x in xor).count(' the '):
            return sum(xor)


# key = (103,111,100)
if __name__=='__main__':
    print(answer())