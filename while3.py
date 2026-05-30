num=int(input("Enter your number"))
s=0
temp=num
while temp>0:
    digit=temp%10
    s+=digit**3
    temp//=10
if num==s:
    print(num,"it is an armstrong")
else:
    print(num,"It is not an armstrong")