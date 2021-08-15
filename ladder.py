n = int(input())
points = list(map(int, input().split()))

# Way 1
a, b = 0, points[0]
for point in points[1:]:
    a, b = b, max(a, b) + point

print(b)

# Way 2
max_points = [0, points[0]]
for point in points[1:]:
    max_points.append(max(max_points[-1], max_points[-2]) + point)

print(max_points[-1])