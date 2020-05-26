a = [-5,7,1,1,3]
def is_uppercase(inp):
    i = 0
    string = ""
    while i < len(inp):
        if inp[i].islower() == True:
            string += inp
        i += 1
    if len(string) > 0:
         return False
    else:
        return True

is_uppercase(a)