def func(val1 , val2 , h):
    area = 0.5 * (val1+val2) * h 
    return area

val1 = float(input())
val2 = float(input())
h = float(input())
answer = func(val1 , val2 , h)
print(answer)