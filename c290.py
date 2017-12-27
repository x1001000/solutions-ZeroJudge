while True:
    try:
        X = input()
    except:
        break
    i, A, B = 0, 0, 0
    for x in X:
        i += 1
        if i%2==1:
            A += int(x)
        else:
            B += int(x)
    print( abs(A-B) )