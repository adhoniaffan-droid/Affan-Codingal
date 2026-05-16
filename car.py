print("select your ride")
print("1. car")
print("2. bike")
choice=int(input("enter your choice"))
if choice==2:
    print("what type of bike")
    print("1. mountain\n")
    print("2. bmx\n")
    choice2=int(input("enter your choice"))
    if choice2==1:
        print("you have selected mountain bike")
    else:
        print("you have selcted bmx bike")
elif choice==1:
    print("what type of car")
    print("1.sedan\n")
    print("2.xuv\n")
    choice3=int(input("enter your choice"))
    if choice==1:
        print("you have selcted a sedan")
    else:
        print("you have selcted a xuv")
else:
    print("wrong choice")