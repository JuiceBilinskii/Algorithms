first = ' ' + input()
second = ' ' + input()

m = len(first)
n = len(second)

table = [[float('inf') for j in range(n)] for i in range(m)]


def get_distance(array, i, j):
    if array[i][j] == float('inf'):
        if i == 0:
            array[i][j] = j
        elif j == 0:
            array[i][j] = i
        else:
            ins = get_distance(array, i, j - 1) + 1
            del_ = get_distance(array, i - 1, j) + 1
            sub = get_distance(array, i - 1, j - 1) + int(first[i] != second[j])
            array[i][j] = min(ins, del_, sub)
    return array[i][j]


for i in range(m):
    for j in range(n):
        get_distance(table, i, j)

print(table[-1][-1])