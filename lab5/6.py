import re
def test(s):    
    check = r'[ ,.]'
    modified_string = re.sub(check, ':', s)    
    return modified_string
s = input()
string = test(s)
print(string)