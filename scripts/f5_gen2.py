def my_range(x): # generator
    start = 0 
    while start < x:
        yield start
        start += 1
        
for i in my_range(5):
    print(i)