'''
list
====
1)List is collection of dissimialr datatype elements.
2)Element in list are enclosed in square brackets.
3)List is mutable.[Once defined they can be changed.]
'''
#Define List

l=[10,89.7,-3,45.6,'itvedant']
print(l)
print(type(l))

#len()

n=len(l)
print("Total Number of Elements in the List:",n)

#indexing
'''
                       l
                       
          [10,89.7,-3,45.6,'Itvedant']
           0   1    2  3       4
           -5  -4  -3  -2      -1
           
Accessing list element
    syntax:

        list_variable[index_value]
'''

#print(1[3])
#print(1[-4])


#Slicing

l1=l[1:4:1]
print(l1)

lrev=l[::-1]
print(lrev)

'''

                       
                       
          [10,89.7,-3,45.6,'Itvedant']
           0   1    2  3       4
'''

#for loop over list
print("With Index:")

for i in range(0,len(l),1):
    print(l[i])

print("Without Index:")
for i in l: #[10,89.7,-3,45.6,'itvedant']
    print(i)

