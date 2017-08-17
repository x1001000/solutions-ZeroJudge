while True:
  try:
    a,b,N=map(int,input().split())
  except:
    break
  answer=str(10**N*a//b)
  n=len(answer)
  if N>=n:
    print('0.'+'0'*(N-n)+answer[-N:])
  else:
    print(answer[:-N]+'.'+answer[-N:])
