def func(str):
   
    words = str.split()

    rev = ' '.join(reversed(words))

    return rev

ur_int = input()
result = func(ur_int)
print(result)