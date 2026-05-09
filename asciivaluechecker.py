char=input("enter a single character")
if type(char) is str and len(char)==1:
    ascii_num=ord(char)
    print("character ",char)
    print("ASCII Value", ascii_num)
else:
    print("enter a valid character")
    