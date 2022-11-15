'''
Need of Logical operator
========================
1)To check more than one condition in conditional statement
  or instruction.
'''

x=10
y=20
z=40

r= x>y and x>z #10>20  and 10>40  => F and F => F
            #100>20 and 100>40 => T and T => T
print(r)

# or Operator

a=10
b=25
c=9

re=a>b  or  a>c  #10>25 or 10>9 => F or T => T
print(re)

#unary operator  => not

renot=not(a>b)  #!(10>25)=>!(False)=True
print(renot)

