a = ["hej", "på", "dig"]
print(a)

temp = a[0]
a[0] = a[2]
a[2] = temp

print(a)