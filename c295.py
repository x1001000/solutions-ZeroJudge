while True:
    try:
        N, M = map(int, input().split())
    except:
        break
    S, M = 0, []
    for _ in range(N):
        x = max(list(map(int, input().split())))
        S += x
        M.append(x)
    line2 = []
    for x in M:
        if S%x==0:
            line2.append(x)
    print(S)
    print( * [-1] if len(line2)==0 else line2 )