'''
A three digit number is enetered through keyboard. Write a
program to
a) reverse that digit.
b) Sum of digits.

a)
     input                      output 
    n=675  -----> logic ------>  576

b)  n=675 ------> logic ------>  6+7+5=18

    675=6*100+7*10+5*1

    576=5*100+7*10+6*1

    sum=6+7+5

    digit separation => % and // with divisor 10
    reverse number formation
'''
x=print("Enter three digits Number:")
x=input()
n=int(x)  #convert string to Integer
a=n%10    #a=5
b=n//10   #b=67
c=b%10    #c=67%10=7
d=b//10   #d=67//10=6

rev=a*100+c*10+d*1      #rev=5*100+7*10+6*1=500+70+6=576
print("Original Number:",n)
print("Reverse Number:",rev)

s=a+c+d    #s=5+7+6=18
print("Summation Of Digits:",s)





