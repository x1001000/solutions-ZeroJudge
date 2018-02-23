while True:
    try:
        N = int(input())
    except:
        break
    friend = list(map(int, input().split()))
    people = set(friend)
    group = 0
    while True:
        try:
            A = people.pop()
        except:
            break
        B = friend[A]
        group += 1
        while A != B:
            people.remove(B)
            B = friend[B]
    print(group)