#1. Write a function for arithmetic operators(+,-,*,/)
a = input('Enter first number: ')
b = input('enter second number')
sum = int(a) + int(b)
# Subtract two numbers
sub = float(a) - float(b)
# Multiply two numbers
mul = float(a) * float(b)
#Divide two numbers
div = eval(a) / eval(b)
print('sum=', sum)
print(sub)
print(mul)
print(div)

#2. Write a method for increment and decrement operators(++, --)
a=0
a+=1
a=a+1
print('The value of a is ',a)
print('INCRE Loop')
for i in range(0,12):
    print(i)
print('DECRE Loop')
for i in range(5,-5,-2):
    print(i)
    # 3. Write a program to find the two numbers equal or not
S= input('enter 1st num')
d= input('enter 2nd num')
if S==d:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")
#4. Program for relational operators (<,<==, >, >==)
a = input('enter 1st num')
b = input('enter 2nd num')
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)

a = int(input('Enter first number= '))
b = int(input('Enter second number= '))
c = int(input('Enter third number= '))
if a > b:
     print('a=:', a, "is greater ")
else:
    print('b=:',b, " is greater ")
if a < b:
     print('a=:',a, "is smaller2 ")
else:
    print('b=:',b, " is smaller ")
if c > a:
    print('c=:',c, "is greater ")
else:
    print('a=:',a, " is greater  ")
if c < a:
        print('c=:', c, "is smaller2 ")
else:
        print('a=:', a, " is smaller ")
if c>b:
    print('c=:',c, "is greater ")
else:
    print('b=:',b, " is greater ")
if c < b:
        print('c=:', c, "is smaller2 ")
else:
        print('b=:', b, " is smaller ")


