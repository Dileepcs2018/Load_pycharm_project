## initializing IP address ip_address = "255.001.040.001"
## spliting using the split() functions
ip_address = "255.001.040.001"
parts = ip_address.split(".")
print(parts)
## converting every part to int
#parts = [int(part) for part in parts]
x = []
for part in parts:
    x.append(int(part))

print("*************", x)
z = []
for y in x:
    z.append(str(y))

print(z)

output = ".".join(z)
print(output)




# ## convert each to str again before joining them
# parts = [str(part) for part in parts]
# print("Dileep------ ", parts)
# ## joining every part using the join() method
# ip_address = ".".join(parts)
# print(ip_address)