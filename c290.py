while True:
    try:
        X = input()
    except:
        break
    i, even, odd = 0, 0, 0
    for x in X:
        if i%2==0:
            even+=int(x)
        else:
            odd+=int(x)
        i+=1
    print(abs(even-odd))