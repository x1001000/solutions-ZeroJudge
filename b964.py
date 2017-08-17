while True:
  try:
    input()
  except:
    break
  grades = sorted( map( int, input().split() ) )
  answer1 = ''
  answer2 = 'best case'
  answer3 = 'worst case'
  for grade in grades:
    answer1 += str(grade) + ' '
    if grade < 60:
      answer2 = grade
    if answer3=='worst case' and grade >= 60:
      answer3 = grade
  print(answer1[:-1])
  print(answer2)
  print(answer3)
