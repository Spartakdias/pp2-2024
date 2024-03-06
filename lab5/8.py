import re
def test(string):    
    check = re.findall('[A-Z][^A-Z]*', string)
    return check
s = input()
string = test(s)
print(string)
