#1. Different ways creating a string
str = 'this is first way'
print(str)
str = "this is second way"
print(str)
str1 = '''this is third way'''
print(str1)
str2 = """this is 
            fourth way"""
print(str2)

#2. Concatenating two strings using + operator
str = "This is python"
str1 = "\this version is 3.10.9"
Con_str = str + str1
print(Con_str)

#3. Finding the length of the string
str = "This is new string"
print(len(str))

#4. Extract a string using Substring


import re
Sub = 'sowmya'
str1 = 'sowmya is studying '
print(re.match(Sub,str1))

#5. Searching in strings using index()
str1 = 'Ashrafi'
str2 = 'sh'
str3 = 'f'
print("Position of sh:",str1.index(str2))
print("Position of f:",str1.index(str3))

#6. Matching a String Against a Regular Expression With matches()

#7. Comparing strings
str1 = 'suzi gowda'
str2 = 'ayana firdos'
str3 = str1
print(str1 == str2)
print(str1 == str3)
print(str2 == str3)
print(str1 != str2)

