weight, n = map(int, input().split())
ingots = list(map(int, input().split()))

# weight, n = 10, 3
# ingots = [4, 1, 8]

table = [[0 for j in range(weight)] for i in range(n)]
# first_row = []

# for i in range(weight):
#     if ingots[0] <= i + 1:
#         first_row.append(ingots[0])
#     else:
#         first_row.append(0)
# table.append(first_row)

# print(table)

for i, ingot_weight in enumerate(ingots):
    for j, current_backpack_capacity in enumerate(range(1, weight + 1)):
        if ingot_weight <= current_backpack_capacity:
            new_backpack_weight = ingot_weight
            i_, j_ = i - 1, j - ingot_weight
            if i_ >= 0 and j_ >= 0:
                new_backpack_weight += table[i_][j_]
            if i > 0:
                table[i][j] = new_backpack_weight if new_backpack_weight > table[i - 1][j] else table[i - 1][j]
            else:
                table[i][j] = new_backpack_weight
        else:
            table[i][j] = table[i - 1][j] if i > 0 else 0

print(table[-1][-1])
