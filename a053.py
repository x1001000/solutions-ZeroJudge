while True:
    try:
        N = int(input())
    except:
        break
    if N <= 10:
        grade = N*6
    elif 11 <= N <= 20:
        grade = 60 + (N-10)*2
    elif 21 <= N <= 40:
        grade = 80 + (N-20)*1
    elif N > 40:
        grade = 100
    print(grade)