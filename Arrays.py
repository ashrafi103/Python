#Write a function to add integer values of an array
a=[24,50,48,52,14,14]
sum=0
for i in range(0,len(a)):
    sum=sum+a[i]
print("Sum of all integer values in array: ", sum)

# Write a function to calculate the average value of an array of integers.
an=[10,21,32,43,54]
sum=0
for i in range(0,len(an)):
    sum=sum+an[i]
    avg=sum/len(an)
print("average value of an array of integers::", avg)

# Write a program to find the index of an array element.
an=[10,21,32,43,54]
index=an.index(21)
print("Index of 21: ",index)
index=an.index(10)
print("Index of 10: ",index)
index=an.index(43)
print("Index of 43: ",index)
# Write a function to test if array contains a specific value.

s=[11,14,17,18,23,48]
if s==18:
        print("Element exist")
else:
    print("Element not exist")
# Write a function to remove a specific element from an array.

s.remove(11)
print(s)
s1=[1,2,4]
s2=[]
s2=s1.copy()
print(s)
print(s2)

# Write a function to find the minimum and maximum value of an array.

arr=[25,110,5,45,49,7,48,77,99,8,4]
minposition =arr.index(min(arr)),min(arr)
print ("The minimum  value and index of array:", minposition)
maxposition =arr.index(max(arr)),max(arr)
print ("The maximum  value and index of array:", maxposition)
# Write a function t reverse and remove array using index
arr.reverse()
print(arr)
arr.remove(arr[1])
print(arr)

# Write a function to find the duplicate values of an array
arr=[25,110,5,45,49,7,48,77,99,8,4,5,25,77]
for i in range(0,len(arr)):
    for k in range(i+1,len(arr)):
        if arr[i] == arr[k]:
            print('duplicate values of an array',arr[k])


# Write a method to find the second largest number in an array.
arr=[25,110,5,45,49,7,48,77,99,8,4,5,25,77]
arr.sort()
print(arr)
print("Second largest number:",arr[-3])

#Write a method to find number of even number and odd numbers in an array.
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
evennums = 0
oddnums= 0
for i in arr:
    if i % 2 == 0:
        evennums += 1
        
    else:
        oddnums += 1
print("Even Numbers in given array:",evennums)
print("Odd Numbers in given array:",oddnums)

# Write a function to get the difference of largest and smallest value.


arr = [10,6,11,13,14]
arr.sort()
print(arr)
arr2=arr[4]-arr[0]
print("Difference of largest and smallest value:",arr2)

# Write a method to verify if the array contains two specified elements(12,23).

arr=[11,12,20,24,23]
for i in arr:
    for i in arr:
        if i == 12:
            print("Exist in array")
        if i == 23:
            print("Exist in array")


#Write a program to remove the duplicate elements and return the new array


arr=[25,110,5,45,49,7,48,77,99,8,4,5,25,77]
newarr=[]
for k in range(0,len(arr)):
    for j in range(k+1, len(arr)):
        if arr[k] ==arr[j]:
            print('duplicate elements=',arr[j])
newarr=[set(arr)]
print('new list elements=',newarr)

