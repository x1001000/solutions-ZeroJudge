while True:
  try:
    N, K = input().split()
  except:
    break
  N, K = int(N), int(K)
  X = sorted([int(float(x)) for x in input().split()])
  upper = X[-1]-X[0]
  lower = 0
  while lower < upper-1:
    test = (upper+lower)//2
    i = 0
    try:
      for _ in range(K):
        x = X[i]
        while X[i] <= x+test:
          i+=1
      lower = test
    except:
      upper = test
  print(upper)
  '''
  取得輸入的第一行，轉整數存入N和K
取得輸入的第二行，排序存入X
用二分逼進法，找最小直徑
上界upper初始值為左右兩端座標距離
下界lower初始值為0
當下界小於上界減一時就二分逼進
test為upper和lower的平均值
作為基地台直徑去嘗試覆蓋服務點
若覆蓋不到最右端服務點
則test更新lower
若覆蓋超過最右端服務點
則test更新upper
直到下界和上界為相鄰整數
輸出上界upper
'''
