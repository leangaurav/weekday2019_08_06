#1
s1 = 'Gaurav'
s2 = 'tuteur.py@gmail.com'
print(len(s1), len(s2))

#2 input a string and print it's length
x = input('Enter anything: ')
print(len(x))

#3 input 2 numbers and print their sum and difference
inp1 = int(input('enter number1 : '))
inp2 = int(input('enter number2 : '))
sum = inp1 + inp2
print('sum is', sum)
diff = inp1 - inp2
print('diff is', diff)

#4
s1 = 'ab'
s2 = 'de'
s3 = s1 + s2
print(s3)

#6
s1 = 'ab'*4
print(s1)

#7
s1 = 'ab\n'*4
print(s1)

#8
s = input('enter a string: ')
n = int(input('enter number: '))
print(s*n)

#9
res = print('Ashok')
print(res)


#10
res = len('tuteur.py@gmail.com')
print(type(res))

#11
s1 = 'Gaurav'
s2 = 'tuteur.py@gmail.com'
s3 = s1 + '\n' + s2
print(type(s3))
print(len(s3))

#12 
import math
math.sqrt(4)

#13
import math
n = int(input('enter a number: '))
math.sqrt(n)


#14
n1 = int(input('enter number1: '))
n2 = int(input('enter number2: '))
n3 = int(input('enter number3: '))
n4 = int(input('enter number4: '))
sum = n1+n2+n3+n4
avg = sum/4
print(avg)

#15
help(abs)

#16. What is the output of this code when run from python interpreter.
#	print(__name__)
'__main__'

#17. What is the output of this code when run from a python script.
#	print(__name__)
'__main__'

#18. Does the dir of int class contain an attribute __name__ (Y/N).
'Answer is No'

#19. Predict the output of:
print(__name__)
print(__builtins__.__name__)
print(int.__name__)