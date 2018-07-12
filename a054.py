numbers=[10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33]
while True:
    try:
        ID = input()
    except:
        break
    for number in numbers:
        sumup = number//10 + (number%10)*9
        n = 8
        for x in ID[:-1]:
            sumup += int(x)*n
            n -= 1
        sumup += int(ID[-1])
        if sumup%10 == 0:
            print(chr(numbers.index(number)+65), end='')
    print()
