def f(x):
    result = ''
    count = 0
    digit = x[0]
    for i in range(len(x)):
        if x[i] == digit:
            count += 1
        else:
            result += str(count) + str(digit)
            count = 1
            digit = x[i]
    result += str(count) + str(digit)
    return result

series = ['1001000', '1']
for _ in range(39):
    series.append(f(series[-1]))

while True:
    try:
        n = int(input())
    except:
        break
    print(series[n])
