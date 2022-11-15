'''
In user input of a=70,b=50,c=20
First if condition is evaluated to be True and we
got the result of greatest of three numbers.

If we got the result in first if condition, then
ideally there is no need to check further if conditions.
Since in above program its checking other two condition,
there is waster of interpreter time in code execution
which is not  going to give us output.

'''

a=int(input("Enter First Number:"))#80
b=int(input("Enter second Number:"))#60
c=int(input("Enter Third Number:"))#110

if a>b and a>c:#80>60 and 80>110 => T and F =>F
     print(a,"is Greater")

elif b>a and b>c:#60>80 and 60>110 => F and F =>F
     print(b,"is Greater")

elif c>a and c>b:#110>80 and 110>60 => T and T =>T
     print(c,"is Greater")  
