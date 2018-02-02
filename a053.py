while True:
    try:
        N = int(input())
    except:
        break
    if N <= 10:               #因為第6,8,10,12行的條件彼此不重疊
        grade = N*6
    elif 11 <= N <= 20:       #所以第8,10,12行的elif寫成if也行
        grade = 60 + (N-10)*2
    elif 21 <= N <= 40:       #雖然結果是一樣的，但意義不同
        grade = 80 + (N-20)*1
    elif N > 40:              #從一個有四個可能性的問題變四個問題
        grade = 100
    print(grade)