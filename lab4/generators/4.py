def square(a,b):
    for i in range(a,b+1):
        yield i**2

a = int(input())
b = int(input())

gen = square(a,b)
for i in gen:
    print(i)