while True:
  try:
    N=int(input())
  except:
    break
  direct=int(input())
  step=[[-1,0],[0,-1],[1,0],[0,1]]
  matrix=[]
  for _ in range(N):
    matrix.append(input().split())
  x,y=N//2,N//2
  output=matrix[y][x]
  move=1
  moves=1
  while moves<N**2:
    for _ in range(2):
      for _ in range(move):
        if moves<N**2:
          moves+=1
          x+=step[direct][0]
          y+=step[direct][1]
          output+=matrix[y][x]
      direct+=1
      direct%=4
    move+=1
  print(output)
'''
輸入字串轉成整數存入N
發生EOF時跳出迴圈
輸入方向
設step依序為向左向上向右向下移動一步
N次input將二維陣列存入matrix
走訪起點存入output
move為同向走幾步，初始值1
moves為已經走幾步，初始值1
15～25行就是程式語言比人類語言更能表達邏輯的例子
人話不好說 🤣 
輸出output
'''
