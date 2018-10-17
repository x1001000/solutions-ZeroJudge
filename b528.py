from math import *
while True:
    try:
        Y = float(input())
    except:
        break
    try:
        print('{:.2f}'.format(round(acos(asin(Y)) * 180 / pi, 2)))
    except:
        print('FAIL!')
