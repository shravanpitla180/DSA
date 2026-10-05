
'''
Arrays
Data Structures
Collection of elements
we store values in arrays by using index
Index only stores single values
Index starts from 0 to N-1 where N = length of array
Left to Right --> Positive(0 to N-1)
Rigth to Left --> Negative(-1 to -N)
'''
array = [10, 20, 30]
print(array)
print(len(array)) #returning the length of array
print(array[0])   #returning the value by using the index
print(array[1])
print(array[2])

print(array[-1])    
print(array[-2])

array.append(60)    #Adding the value at the end of the list
array.insert(3,35)  #Adding value at the particular mentioned index
print(array)

array.remove(35)
array.pop()
array.pop(2)
print(array)

#Access by value
for x in array:
    print(x)

#Access by index
for i in range(len(array)):
    print(array[i])

#Reverse access 
#access by value
for i in reversed(array):
    print(i)

#access by index
for i in range(len(array) -1, -1, -1):
    print(array[i])

