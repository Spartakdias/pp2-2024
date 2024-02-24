def func(n):
    for i in range(0 , n+1):
        if i%4==0 and i%3==0:
            yield i

n = int(input())
gen = func(n)
for i in gen:
    print(i)