def squares(n):
    for i in range(1 , n+1):
        yield(i**2)

n = int(input())
gen = squares(n)

for i in gen:
    print(i)