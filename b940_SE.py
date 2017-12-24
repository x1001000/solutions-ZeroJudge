def gcd(a,b):
    return b if a%b==0 else gcd(b,a%b)
while True:
    try:
        n = int(input())
    except:
        break
    answer = 0
    for i in range(2,n):
        if gcd(i,n) == 1:
            answer += 1
    print(answer+1)