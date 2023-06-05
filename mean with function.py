def calmean(a,b):
    mean=((a+b)/2)
    print(mean)
a,b=list(map(int,input().split()))
calmean(a,b)
while 1:
 print("if u want more mean press y or not press n")
 x=input()
 if x=="y":
    c,d=list(map(int,input().split()))
    calmean(c,d)
 else:
    break

