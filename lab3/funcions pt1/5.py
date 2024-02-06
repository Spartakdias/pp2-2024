from itertools import permutations

def func(str):
    perms = permutations(str)

    for i in perms:
        print(''.join(i))
 
ur_int = input()
func(ur_int)