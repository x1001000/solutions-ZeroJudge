def is_Armstrong(X):
    Y = 0
    for x in str(X):
        Y += int(x)**len(str(X))
    return True if X == Y else False

while True:
    try:
        n, m = input().split()
    except:
        break
    
    Armstrong_numbers = []
    for i in range(int(n), int(m)+1):
        if is_Armstrong(i):
            Armstrong_numbers.append(str(i))
    
    if Armstrong_numbers:
        print(' '.join(Armstrong_numbers))
    else:
        print('none')
