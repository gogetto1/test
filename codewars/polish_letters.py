"""import unicodedata

def correct_polish_letters(st): 
    
    return unicodedata.normalize('NFKD', st).encode('ascii', 'ignore')

print(correct_polish_letters("Łukasz Dacz"))

print(unicodedata.normalize('NFKD', 'Łukasz Dacz').replace('ł', 'l').encode('ascii', 'ignore')[0:])
"""
# rozwiazanie 1


def correct_polish_letters1(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))


# rozwiazanie 2

def correct_polish_letters2(st):
    l = "ąćęłńóśźż"
    lt = "acelnoszz"
    for i in range(len(l)):
        st = st.replace(l[i], lt[i])
    return st


print(correct_polish_letters1("Łukasz Dacz"))
print(correct_polish_letters2("Łukasz Dacz"))
