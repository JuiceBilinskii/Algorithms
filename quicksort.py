def quicksort(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i <= pivot]
        greater = [i for i in nums[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


array = [4, 7, 2, 78, 4, 5, 7, 2, 5, 94, 34, 23]
print(quicksort(array))
