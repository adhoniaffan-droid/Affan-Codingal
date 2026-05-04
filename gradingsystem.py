print("enter marks obtained in five subjects")
markone =int(input())
marktwo=int(input())
markthree=int(input())
markfour=int(input())
markfive=int(input())

tot=markone+marktwo+markthree+markfour+markfive
avg=tot/5

if avg>=91 and avg <=100:
    print("grade is A")
elif avg>=71 and avg<=91:
    print("grade is B")
elif avg>=51 and avg<=71:
    print("grade is C")
elif avg>=33 and avg<=51:
    print("grade is D")
elif avg>=21 and avg<=33:
    print("grade is E")
else:
    print("invalid input")