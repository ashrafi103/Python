'''word='Bright IT Career'
for i in range(10):
    print(word)'''
'''a=0
while(a<=20):

    print(a)
    a+=1'''
'''s=15
d=18
print(s==d)
print(s!=d)'''
'''Numbers = [1,2,3,4,5,6,7,8,9,10,14,13,17]
print("Even Numbers: ")
for i in Numbers:
    if i % 2 == 0:
        print(i, end =" ")
print("\nOdd Numbers:")
for i in Numbers:
    if i % 2 != 0:
        print(i, end =" ")'''
'''a=int(input('enter 1st number'))
e=int(input('enter 2nd number'))
d=int(input('enter 3rd number'))
if a>=e and a>=d:
    largestnum=a
elif e>=a and e>=d:
    largestnum = e
else:
    largestnum =d
    print('Largest number is =', largestnum)'''
'''s=10
d=20
print("Even Numbers Between 10 to 20: ",end=" ")
while s <= d:
    if(s % 2 == 0):
        print(s)
    s += 1'''
'''i=1
while True:
    print("Print 1 to 10 using the do-while loop statement:",i)
    i += 1
    if(i>10):
        break'''
'''a = int(input('Enter a number to check if its armstrong or not: '))
sum = 0
temp = a
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if a == sum:
    print(a," is an amstrong number")
else:
    print(a," is not an amstrong number")'''
'''number = int(input("Enter any number to check prime number or not: "))
if (number>1):
        for i in range(5, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
            else:
                print(number, "is a prime number")

else:
    print(number, "is not prime number")'''
'''a= int(input("Enter number to check palindrome or not:"))
temp=a
num1=0'''
'''n = int(input("Enter number to check palindrome or not:"))
temp = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if(temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")'''

    #print("The number isn't a palindrome!")
'''a = int(input('Enter Number to check is EVEN or ODD: '))
if a % 2 == 0:
    print(" {0} is Even ".format(a))
else:
    print(" {0} is odd ".format(a))'''
gender = input('Enter element F OR M')
if (gender == "M"):
    print("male")
else:
   print("female")

