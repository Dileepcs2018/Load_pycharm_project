lst1 = []
a = int(input("enter the number->"))
lst1.append(a)
b = int(input("enter the number->"))
lst1.append(b)
c = int(input("enter the number->"))
lst1.append(c)

lst1.sort()

output = ""
for i in lst1:
    output = output + str(i) + ','

print(output)







