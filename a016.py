def there_is_repeat_in_(a_list):
  return True if len(set(a_list)) < 9 else False
while True:
  try:
    matrix_9x9 = [ input().split() for _ in range(9) ]
    for row in matrix_9x9:
      if there_is_repeat_in_(row):
        print('no')
        break
    else:
      for i,j in zip([0,0,0,3,3,3,6,6,6],[0,3,6]*3):
        matrix_3x3 = matrix_9x9[i][j:j+3] + matrix_9x9[i+1][j:j+3] + matrix_9x9[i+2][j:j+3]
        if there_is_repeat_in_(matrix_3x3):
          print('no')
          break
      else:
        print('yes')
    input() # 輸入中的任兩個矩陣中間有一個空行要已讀它
  except:
    break