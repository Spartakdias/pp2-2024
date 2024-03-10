def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

n = int(input())
list = []
for i in range (1, n+1):
    numbers = int(input())
    list.append(numbers)
result = multiply_list(list)
print(result)