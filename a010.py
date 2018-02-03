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
        n = int(input())
    except:
        break
    factorization = ''
    while n > 1:
        prime = primes.pop(0)
        power = 0
        while n%prime == 0:
            n //= prime
            power += 1
        if power > 0:
            factorization += str(prime)
            if power > 1:
                factorization += '^'+str(power)
            factorization += ' * '
    print(factorization[:-3])