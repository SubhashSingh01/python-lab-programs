import random
print("your otp is-")

for i in range(1):
    out=random.random()
    otp=str(out)
    otp2=otp[2:6]
    print("your otp is",otp2)
g=input("enter m for more otp and n for no more otp")
if g=='m':
          out1=random.random()
          otp1=str(out)
          otp3=otp[2:6]
          print("your otp is",otp3)
