def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def binary_search(nums, val):
    a, b = 0, len(nums) - 1
    while a <= b:
        middle = (a + b) // 2
        if nums[middle] == val:
            return middle
        elif nums[middle] < val:
            a = middle + 1
        else:
            b = middle - 1
    return


print(factorial(5))
print(binary_search(list(range(0, 101, 2)), 100))

a_dict = {1: 'foo', True: 'bar'}
print(a_dict)
foo = [3, 1, 2]