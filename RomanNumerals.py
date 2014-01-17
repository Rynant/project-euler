from collections import OrderedDict

rnchars = ['I','IV','V','IX','X','XL','L','XC','C' ,'CD','D', 'CM', 'M']
rnvals =  [ 1 , 4  , 5 , 9  , 10, 40 , 50, 90 , 100, 400, 500, 900,  1000]
rnumerals = OrderedDict(zip(rnchars, rnvals))


def roman_to_int(rn):
    '''Converts a Roman numeral string to an integer.\nThere is no error checking for invalid roman numerals.'''
    total = 0
    rn = rn.upper()
    while rn:
        if len(rn) > 1 and rnumerals[rn[0]] < rnumerals[rn[1]]:
            total += rnumerals[rn[1]] - rnumerals[rn[0]]
            rn = rn[2:]
        else:
            total += rnumerals[rn[0]]
            rn = rn[1:]
    return total


def int_to_roman(number):
    '''Converts an integer to a Roman numeral string.'''
    index = len(rnchars) - 1
    roman = ''
    while number > 0:
        if number >= rnvals[index]:
            roman += rnchars[index] * (number // rnvals[index])
            number %= rnvals[index]
        index -= 1
    return roman
