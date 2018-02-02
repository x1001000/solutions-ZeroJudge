t = int(input())    #測資第一行轉整數存入t
for _ in range(t):  #range(t)就是0到t-1，依序設為_，第3~9行會跑t次
    a, b, c, d = input().split()
    a, b, c, d = int(a), int(b), int(c), int(d)
    if a-b == b-c == c-d: #若abcd成等差，進入第6行
        e = d + (b - a)
    else:                 #否則，進入第8行
        e = d * (b // a)      #用/除得浮點數，用//除得整數
    print(a, b, c, d, e)