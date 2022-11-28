'''
tuple
=====
1)It is collection of dissimilar datatype elements.
2)Elements in the tuple are enclosed in round brackets [parenthesis]
3)They are immutable.
'''

t=(10,20,'itvedant',89.9,'Eclass')
print(t)
print(type(t))


#len

n=len(t)
print("Total Number of Element in Tuple:",n)


#accessing Tuple element with index
'''
                        t
          (10,20,'Itvedant',89.9,'Eclass')
           0  1      2       3       4
           -5-4     -3      -2      -1

     syntax:

            tuple_variable[index_pos]

            
'''

#Slicing
'''
syntax: tuple_variable[start:stop:step]


Slicing with Positive index.

                     t

          (10,20,'Itvedant',89.9,'Eclass')
           0  1      2       3       4
   
start=>2     stop=>4    step=>1
'''
#t1=t[2:5:1]
#print(t1)

'''
Slicing with negative index.

                     t

          ( 10, 20,'Itvedant',89.9,'Eclass')
            0   1      2       3       4


           -5   -4    -3      -2      -1
step=> negative
conclusion:
if step is positive then start=left  end=right
if step is negative then start=right end=left
'''
'''
#t1=t[::-1]
#print(t1)
'''
'''

'''
#Indexing

'''
Need: To process string character by character , there is need
to access character in the string. Indexing helps you to access
character in the string.
There are two types of indexing
1)Positive indexing
2)Negative indexing

Positive index                    
                       t
          (10,20,'Itvedant',89.9,'Eclass')
           0  1      2       3       4
  



Negative Index                  
                        t
          (10, 20,'Itvedant',89.9,'Eclass')
  
           -5  -4     -3      -2      -1
syntax for accessing:
====================
 string_variable[index_number]
'''
'''
#print(t[3])
#print(t[2])
#print(t[-1])
#print(t[-5])
'''


#For Loop using index
#With index

''
print("With Index:")


#for Loop using index

'''
                    t

          ( 10, 20,'Itvedant',89.9,'Eclass')
            0   1      2       3       4

'''
'''
for i in range(1,len(t),1):

    print(t[i])

#Without index

print("Without index:")

for i in t: #for i in "10, 20,'Itvedant',89.9,'Eclass'"

    print(i)


print(t[4])
t[4]="O" #Item Assignment
print(t[4])   

'''


