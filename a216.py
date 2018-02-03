def f(n):
    return n*(n+1)//2
def g(n):
    g = 0
    for i in range(1,n+1):
        g += f(i)
    return g
while True:
    try:
        n = int(input())
    except:
        break
    print(f(n), g(n))