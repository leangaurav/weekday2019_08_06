#1. Input temperature in Fahrenheit in print in Celsius.
fahrenheit = input("Enter the value: ")
celsius = (fahrenheit-32)/1.8
print(celsius)

#2. Write a program to input a number and print its square and cube.
num = input("Enter a number: ")
square = num*num
print(square)
cube = num*num*num
print(cube)

#3. WAP to input a number n and a number m and print the result of following
# n^2 + m^2
n = input("Enter a number: ")
m = input("Enter a number: ")
# n^2+m^2
res = (n*n) + (m*m)

#4. WAP to input a numbers M and N and print result of M N . (use both ** and pow)
n = input("Enter a number: ")
m = input("Enter a number: ")

print(m**n)
print(pow(m,n))

#5. Write a simple interest calculator.

# p -> Amount, r-> Rate, t-> Time
# formula prt/100
p = input("Enter Amount: ")
r = input("Enter rate: ")
t = input("Enter time duration: ")
interest = (p*r*t)/100
print(interest)

#6. Input Principal, Rate, Time and print Compound Interest and Amount.
#p(1+r/100)^t
p = int(input("Enter Amount: "))
r = int(input("Enter rate: "))
t = int(input("Enter time duration: "))
compound_intrest = p*pow(1+r/100,t)
print('compound intrest: ',compound_intrest)
print('principle amount: ',p)

#7. WAP to print sum of first n natural numbers. (n needs to be taken as input).
num = int(input('Enter n: '))
natural_numbers = range(1, num+1)
print(sum(natural_numbers))

#8. WAP to input 2 numbers and swap them. (write using both normal logic with temp variable and also the pythonic way).
#with temp
a = 10
b = 20
temp = a
a = b
b = temp
print(a,b)
#pythonic way
a = 10
b = 20
b, a = a, b
print(a,b)
#9. WAP to print ascii value of all white-space characters present in python.
print(ord(''))
#110. Input a single character and print its ascii values.
p = input("Enter a single character ")

print(ord(p))

#11. WAP that takes area of a circle and gives back the radius and circumference.
from math import pi
from math import sqrt

area_of_circle = input("Enter area of circle: ")
radius_square =area_of_circle/pi
radius = sqrt(radius_square)
print(radius)
circumference = 2*pi*radius
print(circumference)

#12. We need to input marks in 5 subjects out of 100 and print percentage.
s1 = input("Enter subject1 mark out of 100: ")
s2 = input("Enter subject2 mark out of 100: ")
s3 = input("Enter subject3 mark out of 100: ")
s4 = input("Enter subject4 mark out of 100: ")
s4 = input("Enter subject5 mark out of 100: ")

print('s1 percentage is '+str(s1)+'%')
print('s2 percentage is '+str(s2)+'%')
print('s3 percentage is '+str(s3)+'%')
print('s4 percentage is '+str(s4)+'%')
print('s5 percentage is '+str(s5)+'%')
