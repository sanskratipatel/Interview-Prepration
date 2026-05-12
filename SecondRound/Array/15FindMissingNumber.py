def find_missing_number(arr):

    real_sum = 0
    actual_sum = 0

    n = len(arr)

    for i in range(n + 1):
        real_sum += i

    for num in arr:
        actual_sum += num

    return real_sum - actual_sum