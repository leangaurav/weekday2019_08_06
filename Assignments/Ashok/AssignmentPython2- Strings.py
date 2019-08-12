#1. Guess output of each slice:
s='Python is Object Oriented'
#1.s[-1]
print(s[-1]) #op -> d
#2 s[::-1]
print(s[::-1]) #detneirO tcejbO si nohtyP
#3. s[:-1]
print(s[:-1]) #Python is Object Oriente
#4. s[4:10]
print(s[4:10]) # 'on is '


#2. What error do you see for following statements:
s = ''
print(s[1]) #IndexError: string index out of range

#3. Do you get any error for the following code, if not give the output:
S='Gaurav'
print(s[1]) #NameError: name 's' is not defined

#4. Find output of the following:
#a
s='a b cd'
print(len(s)) # 6
print(s[::2]) # abc
print(len(s[::2])) # 3 
#b
s='a#b#c#d#'
print(s.split()) # ['a#b#c#d#']
print(s.split('#')) # ['a', 'b', 'c', 'd', '']
l=s.split('#')
s='$'.join(l) 
print(s) # 'a$b$c$d$'
#c
S='Gaurav'
S=S[::-2][::-2] # 'av'
print(S)
#d
print(1>2) #False
#e
	
#f
s='abcba'
s.upper()
print(s) # abcba
print(s.count('A'), end = ' ,') #0
print(s.count('A', 2,4) , end = ' ,') #0
print(s.count('a', 2,4) , end = ' ,') #0

#5. WAP to input a string and remove all spaces from it.
s1 = input("Enter a string: ")
print(s2.replace(' ',''))
#6. What does this symbol denote: 
# [] List
#7. WAP to print all methods(functions/operations) available in a string (Hint : dir())
print(dir(str))
#8. Write statement to check if rstrip method is available in the str class.
f = dir(str)
if 'rstrip' in f:
    print('rstrip method in str')
else:
    print('rstrip method not in str')

#9. WAP to store the following patterns in a string variable and then print them:

t = '*****\n  *  \n  *  \n  *  \n  *  \n'
print(t)
m = '*     *\n* * * *\n*  *  *\n*     *'
print(m)
l = '  ______\n   |    |\n   o    |\n  /|\   |\n  / \   |\n________|'
print(l)

#10. WAP to input a string and replace all space with new lines (\n) and print again.
s1 = input("Enter a string: ")

if ' ' in s1:
   print(s.replace(' ', '\n'))

#11. WAP to input complete name(first and last name separated by space) and print first and last
#name separately along with their length in upper case.
first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
print('complete name', first_name+' '+last_name)
print('first name',len(first_name), first_name.upper())
print('last name',len(last_name), last_name.upper())

#12. WAP to input a string and split it into 2 halves. The string can be of any length
full_string = input('Enter string: ')
s1, s2 = full_string[:len(full_string)/2], full_string[len(full_string)/2:]