import re
def test(s):
    check = r'a.*b$'
    if re.match(check, s):        
        return True
    else:        
        return False
s = input()
string = test(s)
print(string)



0 1 0+1

def fib(n , s):
    for i in range(s , n+1):
        yield s+n

s = int(input())
n = int(input())
answer  = fib(n , s)
for i in answer:
    print(i)