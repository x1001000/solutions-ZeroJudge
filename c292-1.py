def m(x,y):
    global N
    if 0<=x<N and 0<=y< N:
        return M[x][y]
    else:
        raise BaseException
def add(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1])
u = [(0,-1), (-1,0), (0,1), (1,0)]
while True:
    try:
        N = int(input())
    except:
        break
    d = int(input())
    step = 1
    M = []
    for _ in range(N):
        M.append(list(map(int, input().split())))
    p = (N//2,N//2)
    print(m(*p), end='')
    while True:
        try:
            for _ in range(2):
                for _ in range(step):
                    p = add(p, u[d])
                    print(m(*p), end='')
                d += 1
                d %= 4
            step += 1
        except:
            break