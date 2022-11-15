n=845
a=n%10    #a=5
b=n//10   #b=84
c=b%10    #c=84%10=4
d=b//10   #d=84//10=8

rev=a*100+c*10+d*1   #rev=5*100+4*10+8*1=500+40+8=548
print("Original Number:",n)
print("Reverse Number:",rev)

s=a+c+d    #s=5+4+8=17
print("Summation Of Digits:",s)
