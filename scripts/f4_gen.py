def funct():
    yield 1
    yield 2
    yield 3
    
r = funct() # generator object
print(r)

print(next(r))
print(next(r))
print(next(r))
#print(next(r))

print()
for data in funct():
    print(data)