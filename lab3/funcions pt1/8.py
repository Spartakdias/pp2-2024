def func(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i+2] == 7:
            return True
    return False

numbers = []
for i in range(1000):
    numbers.append(i)
result = func(numbers)
print(result)