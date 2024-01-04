num=10001
a=1001
while a!=0:
    j=a%10
    if j!=0 and j!=1:
        print(f"{a} is not binary")
        break
    else:
        a=a//10
print("binary")