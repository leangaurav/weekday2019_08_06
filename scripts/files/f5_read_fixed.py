f = open('tables.txt', 'r')
print(f.tell())

s = f.read(10) # reads all content in form of a string

while s:
    print('\n Tell:', f.tell())

    print(s, end = '')
    s = f.read(10)
    

f.close()