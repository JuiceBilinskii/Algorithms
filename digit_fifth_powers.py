total_sum = 0
numbers = []
for i in range(2, 1000000):
    digits = map(int, list(str(i)))
    digits_sum = sum((digit**5 for digit in digits))
    if i == digits_sum:
        total_sum += i
        numbers.append(i)
print(total_sum, numbers)