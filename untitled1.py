

x = [
    'bba',
    'a',
    'abb',
    'bb',
]

x = sorted(x,key=lambda a:sum(''.join(x).count(b) for b in a))
print(x)