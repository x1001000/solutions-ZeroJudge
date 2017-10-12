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
    for _ in range(move):
      if moves<N**2:
        moves+=1
        x+=step[direct][0]
        y+=step[direct][1]
        output+=matrix[y][x]
    direct+=1
    direct%=4
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
