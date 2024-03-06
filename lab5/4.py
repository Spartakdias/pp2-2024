import re
def test(s):
    check = re.compile(r'[A-Z][a-z]+')
    sequences = check.findall(s)   
    return sequences
s = input()
string = test(s)
print(string)