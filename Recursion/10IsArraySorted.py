def is_array_sorted(nums, n):
    if n == 0 or n == 1:
        return True
    return (nums[n-1] >= nums[n-2] and is_array_sorted(nums, n-1))

num = [1, 2, 3, 41, 5]
print(is_array_sorted(num, len(num)))