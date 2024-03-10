def fib(n):
    for i in range(0 , n+1):
        yield i

n = int(input())
answer  = fib(n)
for i in answer:
    print(i)