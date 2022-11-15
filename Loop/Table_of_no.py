'''
print table of any number entered by user.
step1: Example
      2=2*1    3=3*1
      4=2*2    6=3*2
      6=2*3    9=3*3
      8=2*4    .
     10=2*5    .     ====> r=2*i where i takes value from 1 to 10
     12=2*6    .
     14=2*7    .
     16=2*8    .
     18=2*9    .
     20=2*10  30=3*10
step2:     repeatition=>loop

     loop
     1)initialization  i=1
     2)condition       i<=10
     3)incre/decre     i+=1 or i=i+1
step3:
     body=> code to be repeated
     r=2*i
'''

n=int(input("Enter a Number:"))
i=1

while i<=10:

    r=n*i
    print(r)

    i+=1
'''
print table of any number entered by user.
step1: Example
      2=2*1    3=3*1
      4=2*2    6=3*2
      6=2*3    9=3*3
      8=2*4    .
     10=2*5    .     ====> r=2*i where i takes value from 1 to 10
     12=2*6    .
     14=2*7    .
     16=2*8    .
     18=2*9    .
     20=2*10  30=3*10
step2:     repeatition=>loop

     loop
     1)initialization  i=1
     2)condition       i<=10
     3)incre/decre     i+=1 or i=i+1
step3:
     body=> code to be repeated
     r=2*i
'''
