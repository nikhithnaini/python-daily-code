a=153
n=153
i=len(str(a))
sum=0
# while a!=0:
#     i=i+1
#     a=a//10
# print(i)

while n!=0:
    b=n%10
    sum=sum+b**i
    n=n//10
if (sum ==a):
    print(f"{a} is armstrong number")
else:
    print("not a armstrong number")
