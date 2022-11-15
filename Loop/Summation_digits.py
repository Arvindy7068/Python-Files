'''

sum of digits entered by the user

876


8+7+6=21


7654     7+6+5+4=22
         ---
          13+5
          ----       ====> s=s+__
           18 + 4
           ------
              22

'''

n=int(input("Enter Number:"))#874
s=0
while n!=0:

      r=n%10
      s=s+r
      n=n//10

print("Sum Of digit is:",s)      

'''
n     n!=0   r=n%10       s=s+r    n=n//10
874 874!=0T  r=874%10=4   s=0+4=4  n=874//10=87
87   87!=0T  r=87%10=7    s=4+7=11 n=87//10=8
8     8!=0T  r=8%10=8     s=11+8=19n=8//10=0
0     0!=0F

'''
