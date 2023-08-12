name = input()
initials = ""
for char in name:
    if ( not char.isupper()):
        initials += char   
print(initials)
