while True:
  try:
    input()
  except:
    break
  X=input().split()
  Y=[]
  group=0
  for x in X:
    if x not in Y:
      Y.append(x)
      index=int(x)
      while X[index]!=x:
        Y.append(X[index])
        index=int(X[index])
      group+=1
  print(group)
