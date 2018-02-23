while True:
    try:
        n = int(input())
    except:
        break
    grades = list(map(int, input().split()))
    grades = sorted(grades)
    print(*grades)
    for i in range(n):
        if grades[i] >= 60:
            print('best case' if i==0 else grades[i-1])
            print(grades[i])
            break
    else:
        print(grades[-1])
        print('worst case')