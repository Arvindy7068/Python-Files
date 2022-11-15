''

Need of conditional statement
==============================
In a program when there is need to take decision based
on certain condition, then there is need of conditional
statement.

what is conditional statement?
=============================
The statement or instruction which helps to give decisionbased on certain condition in a program are called as
conditional statements or conditional instructions or decision control instruction.

Types of conditional statement
=============================
1) if statement
2) if else statement
3) nested if else
4) logical operators
5) elif

if statement
============
syntax:

if condition:

    code in if block

    working:
======
if the condition is True then its execute if block or
program control enter in if block and execute code inside
if block.

if condition is false then it wont execute if block.


if..else
========

syntax:

if condition:

    code in if block

else:

   code in else block
working:
======
if the condition is True then its execute if block or
program control enter in if block and execute code inside
if block.
if the condition is false it execute else block.

'''

#Two Number entered by user. WAP to find greatest of two numbers
'''
print("Enter a Number")
#x=input()
#a=int(x)
a=int(input()) #a=45,10
print("Enter a value")
b=int(input()) #b=30,30

if a>b:#45>30 T,10>30 F
   print("In if block")
   print("Greater is:",a)

else:
     print("In else block")
     print("Greater is:",b)




