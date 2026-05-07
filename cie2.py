s=input("Enter: ")
new=""
for ch in s:
    if ch not in 'aeiouAEIOU':
        new+=ch
print(new)