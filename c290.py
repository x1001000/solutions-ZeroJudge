while True:
  try:
    X=input()
  except:
    break
  i=0
  even=0
  odd=0
  for x in X:
    if i%2:
      even+=int(x)
    else:
      odd+=int(x)
    i+=1
  print(abs(even-odd))
