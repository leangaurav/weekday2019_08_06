f = open('tables.txt', 'r')

s = f.read() # reads all content in form of a string

print(s)
print(repr(s))

f.close()