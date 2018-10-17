def every_month():
    global N, fuel, month
    fuel -= N+1
    month += 1
    N = int(fuel/5)-1 if fuel%5==0 else int(fuel/5)
    if fuel==0:
        return 'Mid2 94 Mid2'
    every_month()

while True:
    N = int(input())
    if N == -1:
        break
    fuel = (N+1)*5
    month = 0
    every_month()
    print(month)
