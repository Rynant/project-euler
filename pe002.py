def fibeven(max):
    a, b = 2, 8
    while a < max:
        yield a
        a, b = b, b * 4 + a
        
def answer():
    return sum(x for x in fibeven(4000000))

if __name__=='__main__':
    print(answer())