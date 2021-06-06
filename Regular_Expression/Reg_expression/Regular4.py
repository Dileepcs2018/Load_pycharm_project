import re
s = input("enter mobile number")

matcher = re.fullmatch('[6-9]\d{9}',s)
if matcher != None:
    print("Valid mobile number")

