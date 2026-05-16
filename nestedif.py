medical=input("do you have a medical case ").strip().upper()
if medical=="Y":
    print("you are allowed")
else:
    atten=int(input("enter the attendance of the student"))
    if atten>=75:
        print("allowed")
    else:
        print("not allowed")
        