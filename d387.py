
MAX = 1000000
is_prime = [False,False]+[True]*(MAX-1)
primes = []
now = 2
while True:
    primes.append(now)
    for i in range(now*2, MAX+1, now):
        is_prime[i] = False
    now += 1
    try:
        while is_prime[now] == False:
            now += 1
    except:
        break

while True:
    try:
        N = int(input())
    except:
        break
    if is_prime[N]:
        M = int(str(N)[::-1])
        if is_prime[M] and M!=N:
            print('%d is emirp.'%(N))
        else:
            print('%d is prime.'%(N))
    else:
        print('%d is not prime.'%(N))