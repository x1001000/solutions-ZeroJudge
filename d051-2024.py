# http://www.mathland.idv.tw/life/cf.htm
# 攝氏溫度=(華氏溫度+40)÷1.8-40
# f-string可夾帶變數和設定小數點位數

F = int(input())
C = (F + 40) / 1.8 -40
# print(C)
print(f'{C:.3f}')