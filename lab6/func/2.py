def count(str):
    upper = sum(1 for char in str if char.isupper())
    lower = sum(1 for char in str if char.islower())
    return upper, lower

s = input()
result = count(s)
print(result)