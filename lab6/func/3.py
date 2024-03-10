def is_palindrome(str):
    string = str.lower().replace(" ", "")
    if string == string[::-1]:
        return ("Yes")
    else:
        return("No")

s = input()
result = is_palindrome(s)
print(result)