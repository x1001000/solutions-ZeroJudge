table='xxxxxxxxxxABCDEFGHJKLMNPQRSTUVXYWZIO'

ID = input()
code = table.find(ID[0])
total = code//10 + (code%10) * 9

for i in range(1, 9):
    total += int(ID[i]) * (9 - i)

total += int(ID[-1])
#print(total)
if total % 10 == 0:
    print('real')
else:
    print('fake')