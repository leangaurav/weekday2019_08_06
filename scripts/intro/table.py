f = open('tables.txt', 'w')

for i in range(1,11):
    print(2,'X', i, '=', 2*i, file = f)
    
f.close()