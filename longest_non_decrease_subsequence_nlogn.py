# Non-decrease sequence


def binary_search(array, t, index):
    a, b = 0, len(t) - 1
    while a <= b:
        middle = (a + b) // 2
        if array[index] == array[t[middle]]:
            while array[t[middle]] == array[index]:
                middle += 1
            # t[middle] = index
            # break
            return middle
        elif array[index] > array[t[middle]]:
            a = middle + 1
        elif array[index] < array[t[middle]]:
            b = middle - 1
    else:
        # t[a] = index
        return a


numbers = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]
n = len(numbers)
tails = [0]
result = [-1 for i in range(n)]
sequence_length = 0

for i in range(1, n):
    if numbers[i] >= numbers[tails[-1]]:
        result[i] = tails[-1]
        tails.append(i)
        sequence_length += 1
    elif numbers[i] < numbers[tails[0]]:
        tails[0] = i
    else:
        temp = binary_search(numbers, tails, i)
        tails[temp] = i
        result[i] = tails[temp - 1]

print(tails)
print(sequence_length)
print(result)

sequence = []
i = tails[-1]
while i != -1:
    sequence.append(numbers[i])
    i = result[i]
print(sequence)