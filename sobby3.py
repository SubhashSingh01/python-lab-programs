import random
print("your otp is-")
out=random.random()
otp=str(out)
otp2=otp[2:6]
print("your otp is",otp2)
while 3:
    g=input("enter m for more otp and n for no more otp")
    if g=='m':
          out1=random.random()
          otp1=str(out1)
          otp3=otp1[2:6]
          print("your otp is",otp3)
    else:
        break
