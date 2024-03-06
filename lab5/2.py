import re

a = input()
answer = re.fullmatch("a(bb){2 , 3}" , a)
print(answer)
 
