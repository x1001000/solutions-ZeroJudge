number=[10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33]
while True:
    try:
        ID = input()
    except:
        break
    index = ord(ID[0])-ord('A')
    add_up = (number[index]%10)*9 + number[index]//10
    n = 8
    for x in ID[1:-1]:
        add_up += int(x)*n
        n -= 1
    add_up = add_up + int(ID[-1])
    if add_up%10 == 0:
        print('real')
    else:
        print('fake')