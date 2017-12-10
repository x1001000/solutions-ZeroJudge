# (1) 英文代號以下表轉換成數字
number = {  'A':10, 'B':11, 'C':12, 'D':13, 
            'E':14, 'F':15, 'G':16, 'H':17, 
            'I':34, 'J':18, 'K':19, 'L':20, 'M':21, 
            'N':22, 'O':35, 'P':23, 'Q':24,
            'R':25, 'S':26, 'T':27, 'U':28, 
            'V':29, 'W':32, 'X':30, 'Y':31, 'Z':33  }

while True:
    try:
        ID = input()
    except:
        break

# (2) 英文轉成的數字, 個位數乘９再加上十位數的數字
    add_up = (number[ ID[0] ]%10)*9 + number[ ID[0] ]//10

# (3) 各數字從右到左依次乘１、２、３、４．．．．８
    n = 8
    for x in ID[1:-1]:
        add_up = add_up + int(x)*n          # or use +=
        n = n - 1                           # or use -=

# (4) 求出(2),(3) 及最後一碼的和
    add_up = add_up + int(ID[-1])

# (5) (4)除10 若整除，則為 real，否則為 fake
    if add_up%10 == 0:
        print('real')
    else:
        print('fake')