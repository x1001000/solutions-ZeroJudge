T = int(input())
for _ in range(T):
    n = input()
    answer = 1
    for x in n:
        answer = answer * int(x)
    print(answer)