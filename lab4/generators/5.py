def func(n):
    for i in  range(n , -1 , -1):
        yield i

n = int(input())
gen = func(n)
for i in gen:
    print(i) 