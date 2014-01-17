def reverse(n):
    return int(str(n)[::-1])

def answer():
    count = 0
    
    for n in range(5, 10000):
        front = n
        back = reverse(n)
        for i in range(1, 51):
            front = front + back
            back = reverse(front)
            if front == back:
                break
        count += int(i == 50)
    
    return count

if __name__=='__main__':
    print(answer())