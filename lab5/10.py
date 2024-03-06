import re 
 
def test(string): 
    check = re.compile(r'(?<!^)(?=[A-Z])') 
    snake = check.sub('_', string).lower() 
    return snake
 
camel_s = input() 
snake_s = test(camel_s)