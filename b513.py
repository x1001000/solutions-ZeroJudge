MAX = 65535
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

for _ in range(int(input())):
    print('Y' if int(input()) in primes else 'N')