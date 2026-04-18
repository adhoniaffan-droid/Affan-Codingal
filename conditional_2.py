actual_cost=float(input("enter your cost"))
sale_cost=float(input("enter your sale cost"))
if (actual_cost<sale_cost):
    amount=sale_cost-actual_cost 
    print("profit",amount)
else:
    print("no profit")