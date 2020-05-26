def pig_it(text):
    c = ""
    b = text.split()

    i = 0
    while i < len(b):
        for word in b:
            c = c + word[1:]+word[0]+"ay "
            i += 1
    c = c[:-1]

    if "?ay" in c:
        c = c.replace("?ay", "?")
        return c
    elif "!ay" in c:
        c = c.replace("!ay", "!")
        return c
    else:
        return c

#rozwiaanie1:
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

#rozwiazanie 2
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
