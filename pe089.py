from functools import reduce
from RomanNumerals import int_to_roman, roman_to_int

with open('data/pe089_roman.txt', 'r') as r:
    originals = r.read().splitlines()

def answer():
    original_len = reduce(lambda sum, rn: sum + len(rn), originals, 0)
    new_len = reduce(lambda sum, rn: sum + len(int_to_roman(roman_to_int(rn))), originals, 0)
    
    return original_len - new_len

if __name__=='__main__':
    print(answer())