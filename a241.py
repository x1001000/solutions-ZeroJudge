def x2(i):
    global count,n
    if i*2<=n:
        #print("x2",i*2)
        count+=1
        x5(i)
        x2(i*2)

def x5(i):
    global count,n
    if i*5<=n:
        #print("x5",i*5)
        count+=1
        x5(i*5)

m = int(input(''))
for _ in range(m):
    n = int(input(''))
    count = 0
    x2(1)
    print(count)
