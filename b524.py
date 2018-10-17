import array
while True:
    try:
        line  = input()
    except:
        break
    index_of_y = array.array('L', [])
    for i in range(len(line)):
        if line[i] == 'y':
            index_of_y.append(i)
    correct_index_of_y = 0
    move = 0
    for index in index_of_y:
        move += abs(index - correct_index_of_y)
        correct_index_of_y += 3
    print(move)
