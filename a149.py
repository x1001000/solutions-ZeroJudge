T = int(input())
for _ in range(T):
    line = input()
    answer = 1
    for x in line:
        answer = answer * int(x)
    print(answer)