while True:
    try:
        X = input()
    except:
        break
    A, B = 0, 0
    for i in range(len(X)):
        if i%2:
            A += int(X[i])
        else:
            B += int(X[i])
    print( abs(A-B) )