while True:
    try:
        N = int(input())
    except:
        break
    S = set()
    for _ in range(N):
        S = S | set(range(*map(int, input().split())))
    print(len(S))