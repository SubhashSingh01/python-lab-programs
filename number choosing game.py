import random
name=input("enter your name")
print("you have 3 chances to guess the number")
i=3
while(i):
    num=int(input("enter the  no."))
    out=random.randrange(1,100)
    if num==out:
        print("congratulations",name, "you won")
        break;
    elif(num<out):
        print("sorry" ,name ,"your no.is small")
    else:
        print("sorry" ,name, "your no.is large")
    i-=1;
