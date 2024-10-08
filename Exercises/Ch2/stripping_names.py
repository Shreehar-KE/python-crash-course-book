"""
2-7. Stripping Names: Use a variable to represent a person's name, and
include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
"""

name_1 = "\tJoey Tribbiani "
name_2 = " \nPhoebe Buffay "

# Note: underscores($$) are used to show the difference after stripping

print(name_1+"$$")
print(name_1.rstrip()+"$$")
print(name_1.lstrip()+"$$")
print(name_1.strip()+"$$")
print()
print(name_2+"$$")
print(name_2.rstrip()+"$$")
print(name_2.lstrip()+"$$")
print(name_2.strip()+"$$")
