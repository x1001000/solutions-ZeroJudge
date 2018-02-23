def flip(matrix):
    return matrix[::-1]
def rotate(matrix):
    return flip(list(zip(*matrix)))
while True:
    try:
        R, C, M = map(int, input().split())
    except:
        break
    matrix = []
    for _ in range(R):
        matrix.append(list(map(int, input().split())))
    for i in list(map(int, input().split()))[::-1]:
        matrix = rotate(matrix) if i==0 else flip(matrix)
    print(len(matrix), len(matrix[0]))
    for vector in matrix:
        print(*vector)