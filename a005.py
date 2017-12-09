t = int(input())
for _ in range(t):
    a,b,c,d = input().split()
    a,b,c,d = int(a), int(b), int(c), int(d)
    if a-b == b-c == c-d: #等差
        e = d + (b - a)
    else:
        e = d * (b // a) #用/會變成浮點數
    print(a,b,c,d,e)