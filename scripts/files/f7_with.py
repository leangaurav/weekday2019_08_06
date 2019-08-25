with open('tables.txt', 'r') as f: # context Handler
    for s in f:
        print(s, end = '')
    print(f.closed)

print(f.closed)

