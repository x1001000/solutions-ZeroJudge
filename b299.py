for _ in range(int(input())):
    N = int(input().split()[0])
    for w in input().split():
        if N > int(w):
            print('NOOOO!!! JACKY XX!')
            break
    else:
        print('YEEES!!! INKER!')
