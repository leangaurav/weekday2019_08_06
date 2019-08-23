f = open('tables.txt', 'r')

print(f.tell())
for s in f:
    print(s, end = '')
print('\n Tell: ', f.tell())

f.close()