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
