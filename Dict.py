Dict =[(4,'swathi'),(6,'sowmya'),(8,'meena'),(5,'swathi')]
print('the id and name of students:',dict)
#1.1. Adding the values in dictionary

a = "Sowmya"
Dict[2] = a
print("\n I added %s in Dictionary"%a)
print("\n updated dictionary is:",Dict)

#1.2. Updating the values in dictionary
Dict[3] = 'Asha'
print("\n I updated the Dictionary with new value")
print("\n updated dictionary is:",Dict)

#1.3. Accessing the value in dictionary
print("\n This is your value",Dict[1])

#1.4. Create a nested loop dictionary
Dict1 = {1: 'Ashrafi', 2: 'firdos',
        3:{'Age' : 18, 'Branch' : 'MCA', 'Year' : '5TH Year'}}
print("\n Nested loop Dictionary:",Dict1)

#1.5. Access the values of nested loop dictionary
print("\n Perticular value of nested Dictionary is:",Dict1[2])

#1.6. Print the keys present in a particular dictionary
print(Dict.keys())

#1.7. Delete a value from a dictionary
del Dict[6]
print("\n I deleted the value from dictionary")
print("\n updated dictionary is:",Dict)
print("\n Accessing an element of a Nested Dictionary:",Dict1[1])
