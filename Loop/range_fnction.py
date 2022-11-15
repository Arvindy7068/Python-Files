'''
range():This function generate list of numbers in a sequence.
syntax:

     range(start,stop,step)

     start=> initialization
     stop => conditon
     step => increment/decrement [positive or negative]
     
'''
'''
x=list(range(1,20,1)) #start=1,stop=10 and step=1 [increment in step of 1]
print(x)
'''

'''
x=list(range(2,20,2))
print(x)
'''

'''
x=list(range(2,20)) #Default step is 1
print(x)
'''
#no Step and Start
'''
x=list(range(20)) # Deafult Start is 0
print(x)
'''
'''
x=list(range()) #error as range () require at least one argument.
print(x)
'''

x=list(range(0))
print(x)
