while True:
    try:
        X = list(map(int, input()))
    except:
        break
    A, B = sum(X[1::2]), sum(X[::2])
    print(abs(A-B))
