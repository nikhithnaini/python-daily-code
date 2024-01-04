n = int(input("Please give a number: "))
print(f"Before reverse your number is : {n}")
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10       
    n = (n//10)
print(f"After reverse : {reverse}")

# a =12345
# b=str(a)
# print(type(b))        SECOND METHOD
# b=b[::-1]
# print(b)
# c=int(b)
# print(c , type(c))