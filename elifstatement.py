unit=int(input("please enter the number "))
if(unit<50):
    amount=unit*2.6
    sur=25
elif (unit<=100):
    amount=130+((unit-50)*3.25)
    sur=35
elif (unit<=200):
    amount=130+162.5+((unit-100)*5.26)
    sur=45
else:
    amount=130+162.5+526+((unit-200)*8.45)
    sur=75
total=amount+sur
print("electricity bill= ",total)