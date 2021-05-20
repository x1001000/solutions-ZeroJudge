T = int(input())
for i in range(1, T+1):
    a = int(input())
    b = int(input())
    answer = 0
    for x in range(a, b+1):
        if int(x**0.5) == x**0.5:
            answer += x
    print(f'Case {i}: {answer}')
