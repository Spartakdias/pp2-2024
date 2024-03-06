import re
def test(string):
    check = 'ab{2,3}'
    if re.fullmatch(check, string):        
        return True
    else:        
        return False
s = input()
string = test(s)
print(string)
 
