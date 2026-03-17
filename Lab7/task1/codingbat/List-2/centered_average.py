def centered_average(nums):
    nums_sorted = sorted(nums)
    trimmed = nums_sorted[1:-1]  # убираем минимальный и максимальный
    return sum(trimmed) // len(trimmed)