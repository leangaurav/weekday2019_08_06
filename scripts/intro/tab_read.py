f = open("tables.txt","r")

s = f.read(10)

while s:
	print(s, end=" ")
	s=f.read(10)
	
	
f.close()
	