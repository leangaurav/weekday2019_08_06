#1. WAP to create a dictionary of numbers mapped to their negative value for numbers from 1-5.
#The dictionary should contain something like this:
#Do with both with and without range based for loop.

f = {}
for i in range(1,6):
	f[i] = -i
print(f)

#2. Check which of the following declarations will work
#1
d ={1=2,3=4} #wrong
#2
d ={1:2,3:4} #correct
#3
d = {1,2;3,4} #wrong

d = {'a':'A','b':1,c:[1234]} #wrong

d = {'a':'A','b':1,'c':[1234]} #correct

d = dict([(1,2), (2,3)]) #correct

d = dict(((1,2), (2,3))) #correct


### 3
l1 = [1,2,3,4]
l2 = [10,11,12,13]

print(dict(zip(l1,l2)))

### 4
asc = 65
d = {}
while asc:
	d[chr(asc)] = asc
	asc+=1
	if chr(asc) == 'Z':
		break

print(d)
### 5 
val = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
lo = {}
for x in 'aeiou':
	count = 1
	for y in 'Beautiful day':
		if x==y:
			lo[x]=count
			count+=1
print(lo)

#### 6
doc = {}
count = 1
gg='Beautiful day'
for y in gg:
	if y.isalpha():
		doc[y]= gg.count(y)
print(doc)

### 7
d = 'count the words in the sentence in'

dp = d.split()
ee = {}
for x in dp:
	ee[x] = dp.count(x)
print(ee)
