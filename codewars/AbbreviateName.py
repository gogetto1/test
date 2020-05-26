"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F"""


def abrreviate_name(name):
    return ((name.split()[0][0].upper()+"."+name.split()[1][0]).upper())


name = input("Please write your first and last name: ")
print(abrreviate_name(name))
